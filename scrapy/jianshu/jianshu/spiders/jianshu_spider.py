# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import etree
import json
from jianshu.items import JianshuItem

class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        # crawl 模板
        # 使用正则表达式爬取
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/[0-9a-z]{12}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        html = etree.HTML(response.text)
        # title = html.xpath("//h1[@class='_1RuRku']/text()")[0]
        try:
            item = JianshuItem()
            page_data = html.xpath("//*[@id='__NEXT_DATA__']/text()")[0]
            data_dic = json.loads(page_data)
            note_data = data_dic["props"]["initialState"]["note"]["data"]
            user_data = note_data["user"]
            item["title"] = note_data["public_title"]
            item["author_nickname"] = user_data["nickname"]
            item["author_avatar"] = user_data["avatar"]
            item["url"] = response.url
            print(item)
            yield item
        except:
            print("解析数据异常")
        return None
