import scrapy
from ..items import CrawlerItemLifeTime


class ReleasesSpider(scrapy.Spider):
    name = "releases_lt"
    collection_name = 'OutSystems_Releases_LifeTime'
    start_urls = ['https://release.outsystems.net/ReleaseDashboard/O11LTReleasePlan.aspx']

    def start_requests(self):
        urls = ['https://release.outsystems.net/ReleaseDashboard/O11LTReleasePlan.aspx']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//table//tbody/tr'):
            item = CrawlerItemLifeTime()

            item['name'] = row.xpath('td[1]//text()').extract_first()
            item['version'] = row.xpath('td[2]//text()').extract_first()
            item['date'] = row.xpath('td[4]//text()').extract_first()

            yield item
