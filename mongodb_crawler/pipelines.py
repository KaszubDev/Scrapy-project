import pymongo
from scrapy.utils.project import get_project_settings
from .items import CrawlerItemPlatformServer
from .items import CrawlerItemLifeTime
settings = get_project_settings()


class MongodbCrawlerPipeline:

    def __init__(self):
        self.client = pymongo.MongoClient(settings.get('MONGO_DB_URI'))
        self.db = self.client[settings.get('MONGO_DB_NAME')]

    def open_spider(self, spider):
        # Start with a clean database
        self.db[spider.collection_name].delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name == 'releases_ps':
            data = dict(CrawlerItemPlatformServer(item))
            self.db[spider.collection_name].insert_one(data)
            return item
        if spider.name == 'releases_lt':
            data = dict(CrawlerItemLifeTime(item))
            self.db[spider.collection_name].insert_one(data)
            return item
        return item
