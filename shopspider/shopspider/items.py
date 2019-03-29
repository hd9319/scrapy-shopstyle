# -*- coding: utf-8 -*-

import scrapy

class TrendingPage(scrapy.Item):
    page_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class Item(scrapy.Item):
    product_id = scrapy.Field()
    name = scrapy.Field()
    unbranded_name = scrapy.Field()
    price = scrapy.Field()
    salePrice = scrapy.Field()
    currency = scrapy.Field()
    stock = scrapy.Field()
    retailer = scrapy.Field()
    brand = scrapy.Field()
    categories = scrapy.Field()
    image_address = scrapy.Field()
    most_recent_drop = scrapy.Field()
