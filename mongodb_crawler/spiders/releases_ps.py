import scrapy
from ..items import CrawlerItemPlatformServer


class ReleasesSpider(scrapy.Spider):
    name = "releases_ps"
    collection_name = 'OutSystems_Releases_PlatformServer'
    start_urls = ['https://release.outsystems.net/ReleaseDashboard/O11PSReleasePlan.aspx']

    def start_requests(self):
        urls = ['https://release.outsystems.net/ReleaseDashboard/O11PSReleasePlan.aspx']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//table//tbody/tr'):
            item = CrawlerItemPlatformServer()

            item['name'] = row.xpath('td[1]//text()').extract_first()
            item['version'] = row.xpath('td[2]//text()').extract_first()
            item['date_cloud'] = row.xpath('td[3]//text()').extract_first()
            item['date_on_prem'] = row.xpath('td[4]//text()').extract_first()

            yield item
