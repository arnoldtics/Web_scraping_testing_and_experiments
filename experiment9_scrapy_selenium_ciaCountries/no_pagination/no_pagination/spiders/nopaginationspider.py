from typing import Iterable
import scrapy
from no_pagination.items import CountriesItem
from urllib.parse import urljoin
from no_pagination.urls import urls

class CountriesSpider(scrapy.Spider):
    name = "countries"

    def start_requests(self):
        for url in urls: yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = CountriesItem()

        def exchange(query):
            coin = response.xpath(query + "/following-sibling::p[1]/text()").get()
            if coin is None: return ""
            if coin.strip() == "the US dollar is used": return "1"
            return response.xpath(query + "/following-sibling::p[1]/text()[2]").get(default='').strip()
        
        item['name'] = response.xpath("//h1[@class='hero-title']/text()").get(default='').strip(),
        item['area'] = response.xpath("//div[@id='geography']//h3[a[text()='Area']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['population'] = response.xpath("//*[@id='people-and-society']//h3[a[text()='Population']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['gdp'] = response.xpath("//*[@id='economy']//h3[a[text()='Real GDP per capita']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['unemployment_rate'] = response.xpath("//*[@id='economy']//h3[a[text()='Unemployment rate']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['taxes'] = response.xpath("//*[@id='economy']//h3[a[text()='Taxes and other revenues']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['debt'] = response.xpath("//*[@id='economy']//h3[a[text()='Debt - external']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['exchange_rates'] = exchange("//*[@id='economy']//h3[a[text()='Exchange rates']]"),
        item['internet_users'] = response.xpath("//*[@id='communications']//h3[a[text()='Internet users']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['porcentaje_internet'] = response.xpath("//*[@id='communications']//h3[a[text()='Internet users']]/following-sibling::p[1]/text()[2]").get(default='').strip(),
        item['airports'] = response.xpath("//*[@id='transportation']//h3[a[text()='Airports']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['roadways_total'] = response.xpath("//*[@id='transportation']//h3[a[text()='Roadways']]/following-sibling::p[1]/text()").get(default='').strip(),
        item['military_expenditures'] = response.xpath("//*[@id='military-and-security']//h3[a[text()='Military expenditures']]/following-sibling::p[1]/text()").get(default='').strip(),
        
        flagLink = response.xpath("//*[@id='main-content']/div/section/div/div[2]/div[1]/section/div/div[1]/div/div/div/picture/img").xpath('@data-src').get()
        if flagLink: flagLink = urljoin(response.url, flagLink)
        item['image_urls'] = [flagLink] if flagLink else []

        item['images'] = None
        item["image_name"] = None


        yield item
