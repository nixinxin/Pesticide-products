# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapy import Request, Spider
from scrapy_redis.spiders import RedisSpider
from nongyao.items import NongyaoItem, CustomLoader


class SpiderSpider(RedisSpider):

    name = 'spider'
    allowed_domains = ['data.miit.gov.cn']
    start_urls = ['http://data.miit.gov.cn/resultSearch?categoryTreeId=1076&pagenow={}']
    redis_key = "spider:start_urls"

    def start_requests(self):
        for i in range(1, 704):
            yield Request(self.start_urls[0].format(i))

    def parse(self, response):
        for i in range(1, 31):
            items = CustomLoader(item=NongyaoItem(), response=response)
            items.add_xpath('province', '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[2]/text()'.format(i))
            items.add_xpath('company', '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[3]/text()'.format(i))
            items.add_xpath('category', '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[4]/text()'.format(i))
            items.add_xpath('title',  '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[5]/text()'.format(i))
            items.add_xpath('product_type', '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[6]/text()'.format(i))
            items.add_xpath('product_id', '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[7]/text()'.format(i))
            items.add_xpath('add_time', '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[8]/text()'.format(i))
            items.add_xpath('expired', '//*[@id="page-wrapper"]/div[2]/table/tbody/tr[{}]/td[9]/text()'.format(i))
            yield items.load_item()

