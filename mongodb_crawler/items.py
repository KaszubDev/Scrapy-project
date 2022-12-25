# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItemPlatformServer(scrapy.Item):
    name = scrapy.Field()
    version = scrapy.Field()
    date_cloud = scrapy.Field()
    date_on_prem = scrapy.Field()
    pass


class CrawlerItemLifeTime(scrapy.Item):
    name = scrapy.Field()
    version = scrapy.Field()
    date = scrapy.Field()
    pass
