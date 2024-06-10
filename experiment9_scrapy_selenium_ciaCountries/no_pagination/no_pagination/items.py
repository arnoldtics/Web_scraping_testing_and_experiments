# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountriesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    area = scrapy.Field()
    population = scrapy.Field()
    gdp = scrapy.Field()
    unemployment_rate = scrapy.Field()
    taxes = scrapy.Field()
    debt = scrapy.Field()
    exchange_rates = scrapy.Field()
    internet_users = scrapy.Field()
    porcentaje_internet = scrapy.Field()
    airports = scrapy.Field()
    roadways_total = scrapy.Field()
    military_expenditures = scrapy.Field()
            
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()
    
