# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 模型数据层，主要是封装爬去到的数据然后写入数据库
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = cover_url = jump_url = title = score = scrapy.Field()
