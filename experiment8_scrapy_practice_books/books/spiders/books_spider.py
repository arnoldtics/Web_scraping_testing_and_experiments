import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'https://books.toscrape.com/',
    ]

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get()[1:],
                'rating': book.css('p').attrib["class"].split()[-1],
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)