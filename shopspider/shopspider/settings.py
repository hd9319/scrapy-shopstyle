# -*- coding: utf-8 -*-

# Scrapy settings for shopspider project

BOT_NAME = 'shopspider'
SPIDER_MODULES = ['shopspider.spiders']
NEWSPIDER_MODULE = 'shopspider.spiders'
USER_AGENT = 'shopspider'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 32

ITEM_PIPELINES = {
   'shopspider.pipelines.TrendingPagePipeline': 200,
   'shopspider.pipelines.ProductPipeline': 200,
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3
AUTOTHROTTLE_MAX_DELAY = 30

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

#SPIDER_MIDDLEWARES = {
#    'shopspider.middlewares.ShopspiderSpiderMiddleware': 543,
#}

#DOWNLOADER_MIDDLEWARES = {
#    'shopspider.middlewares.ShopspiderDownloaderMiddleware': 543,
#}
