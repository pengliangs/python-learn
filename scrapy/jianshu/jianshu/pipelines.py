# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class JianshuPipeline(object):

    def __init__(self):
        con_param = {
            "host":"127.0.0.1",
            "port":3306,
            "database":"jianshu",
            "user":"root",
            "password":"root"
        }
        self.db = pymysql.connect(**con_param)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        try:
            insert_sql = "INSERT INTO `jianshu_article_base_info` (`author_nickname`,`author_avatar`,`title`,`url`)\
                 VALUES (%s, %s, %s,%s)"
            self.cursor.execute(insert_sql,(item["author_nickname"],item["author_avatar"],item["title"],item["url"]))
            self.db.commit()
        except:
            print("执行SQL异常")
            self.db.rollback()

        return item
