# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from MySQLdb.cursors import DictCursor
from twisted.enterprise import adbapi


class NongyaoPipeline(object):

    collection_name = 'nongyao'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(host=settings["MYSQL_HOST"],
                       db=settings["MYSQL_DBNAME"],
                       user=settings["MYSQL_USER"],
                       passwd=settings["MYSQL_PASSWORD"],
                       charset='utf8',
                       cursorclass=DictCursor,
                       use_unicode=True)
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):  # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):   # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):  # 执行具体的插入, 根据不同的item构建不同的sql语句并插入到mysql中
        insert_sql = item.get_sql()
        result = cursor.execute(insert_sql)
        print(result, list(item.values()))