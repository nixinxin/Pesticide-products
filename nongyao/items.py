# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from datetime import datetime


def totime(value):
    value = datetime.strptime(value, '%Y-%m-%d')
    return value


def strips(value):
    return value.strip()


class CustomLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(strips)


class NongyaoItem(scrapy.Item):
    # define the fields for your item here like:
    province = scrapy.Field()
    company = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    product_type = scrapy.Field()
    product_id = scrapy.Field()
    add_time = scrapy.Field()
    expired = scrapy.Field()

    def get_sql(self):
        sql = """insert into chartsite.`nongyao`(`product_type`, `title`, `expired`, `product_id`, `category`, 
        `company`, `add_time`, `province`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}') ON 
        duplicate KEY UPDATE `product_id`= VALUES(`product_id`) """
        sql = sql.format(self['product_type'], self['title'], self['expired'], self['product_id'], self['category'], self['company'], self['add_time'], self['province'])
        return sql

