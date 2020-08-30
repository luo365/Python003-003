# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.spiders import Spider
import json
import pymysql
from douban_prj.items import DoubanPrjItem


class DoubanPrjPipeline(object):
    def process_item(self, item, spider):
        with open('e:/douban.txt', 'a+', encoding='utf8') as f:
            title = item['title']
            director = item['director']
            rate = item['rate']
            output = f't: {title}, d: {director}, r: {rate}\n'
            f.write(output)
        return item


class DoubanMovieMySQLPipeline(object):
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('HOST'),
            user=crawler.settings.get('USER'),
            password=crawler.settings.get('PASSWORD'),
            db=crawler.settings.get('DB')
        )

    def open_spider(self, spider):
        self.con = pymysql.connect(
            self.host, self.user, self.password, self.db)

    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        sql = "INSERT INTO t_movie (title, director, rate) VALUES (%s, %s, %s)"
        val = (item['title'], item['director'], item['rate'])
        with self.con.cursor() as cur:
            cur.execute(sql, val)
        self.con.commit()
