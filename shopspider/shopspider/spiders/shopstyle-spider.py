import os
import json
import math
import scrapy
from items import *

class TrendingSpider(scrapy.Spider):
    name = 'trends_spider'

    NUM_RESULTS_PERPAGE = 50
    NUM_TRENDING_PAGES = 4

    def start_requests(self):
        urls = ['https://www.shopstyle.ca/api/v2/trendPages?indexableOnly=true&limit=%d&offset=%d&pid=shopstyle' % \
                                (self.NUM_RESULTS_PERPAGE, i * self.NUM_RESULTS_PERPAGE ) \
                                for i in range(self.NUM_TRENDING_PAGES)]

        for url in urls:
            yield scapy.Request(url, callback=self.parse)


    def parse(self, response):
        jsonResponse = json.loads(response.body)

        for pageDict in jsonResponse['trendPages']:
            page_id = pageDict['id']
            url = DOMAIN + '/shop/trends/' + pageDict['urlIdentifier']
            title = pageDict['title']
            author = pageDict['author']['firstName'] + ' ' + pageDict['author']['lastName']
            tags = ';'.join(pageDict['tags'])
            trendingPage = TrendingPage(page_id=page_id, url=url, title=title, author=author, tags=tags)
            yield trendingPage

class MenClothesSpider(scrapy.Spider):
    name = 'mens_clothing_spider'

    NUM_MAX_RESULTS = 1000
    NUM_RESULTS_PERPAGE = 100
    PAGE_COUNT = math.ceil(NUM_RESULTS, PAGE_LIMIT)

    def start_requests(self):
        urls = ["https://www.shopstyle.ca/api/v2/products?cat=mens-clothes&includeLooks=true&includeProducts=true&limit=%d&locales=all&offset=%d&pid=shopstyle" \
        % (self.NUM_RESULTS_PERPAGE, self.NUM_RESULTS_PERPAGE * i) for i in range(self.PAGE_COUNT)]

        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        jsonResponse = json.loads(response.body)

        for product in jsonResponse['products']:
            item = _createItem(product)
            yield item

    def _createItem(product):
        product_id = product['id']
        name = product['name']
        unbranded_name = product['unbrandedName']
        price = product['price']
        salePrice = product['salePrice']
        currency = product['currency']
        stock = product['inStock']
        retailer = product['retailer']['name']
        brand = product['brand']['name']
        categories = ';'.join([category['id'] for category in product['categories']])
        image_address = product['image']['sizes']['Large']['url']
        most_recent_drop = product['lastPriceDropDate']['date']
        return Item(product_id=product_id, name=name, unbranded_name=unbranded_name, price=price, salePrice=salePrice, \
                       stock=stock, retailer=retailer, brand=brand, categories=categories, \
                       image_address=image_address, most_recent_drop=most_recent_drop)
