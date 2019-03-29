# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

class TrendingPagePipeline(object):
    def __init__(self, my_setting):
        self.seen_ids = set()
        self.my_setting = my_setting

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        my_setting = settings.get("MY_SETTING")
        return cls(my_setting)

    def process_item(self, item, spider):
        if type(trendingPage).__name__ == 'TrendingPage'
            if item['id'] in self.seen_ids:
                raise DropItem('Duplicate Exists: %s' % item['id'])
            else:
                self.seen_ids.add(item['id'])
                return item


class ProductPipeline(object):
    def __init__(self, my_setting):
        self.seen_ids = set()
        self.my_setting = my_setting

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        my_setting = settings.get("MY_SETTING")
        return cls(my_setting)

    def process_item(self, item, spider):
        if type(trendingPage).__name__ == 'Item':
            if item['id'] in self.seen_ids:
                raise DropItem('Duplicate Exists: %s' % item['id'])
            else:
                self.seen_ids.add(item['id'])
                return item
