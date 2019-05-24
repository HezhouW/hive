# -*- coding: utf-8 -*-

# Scrapy settings for huangye88_fenbu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'huangye88_fenbu'

SPIDER_MODULES = ['huangye88_fenbu.spiders']
NEWSPIDER_MODULE = 'huangye88_fenbu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huangye88_fenbu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

#使用scrapy-redis里面的去重组件.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis里面的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停后,能保存进度
SCHEDULER_PERSIST = True

# 指定排序爬取地址时使用的队列，
# 默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
ITEM_PIPELINES = {
    # 'scrapy_redis.pipelines.RedisPipeline':400,
    'huangye88_fenbu.myPipeLines.mongoPipe.MongopipClass':300,
}

# 指定redis主机
REDIS_HOST='192.168.8.186'
REDIS_PORT=6379

MY_USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Baiduspider-image+(+http://www.baidu.com/search/spider.htm)",
    "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    ]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':300,
    # 'huangye88_fenbu.middlewares.MyproxiesSpiderMiddleware':100,
    'huangye88_fenbu.middlewares.MyUserAgentMiddleware': 400,
}
# 指定mongo
MONGO_HOST = "192.168.14.90"
MONGO_PORT = 27017
MONGO_DBNAME = "test"
MONGO_COLLECTION = "huicong_goods2"

DOWNLOAD_DELAY = 0
CONCURRENT_REQUESTS = 1
RETRY_TIMES = 0