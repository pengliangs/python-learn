# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 项目名称
    name = 'douban_spider'
    # 允许下载域名
    allowed_domains = ['movie.douban.com']
    # 下载首地址
    start_urls = ['http://movie.douban.com/top250']
    # start_urls = ['http://httpbin.org/get'] #测试伪装配置是否生效

    # 下载完成的返回方法
    def parse(self, response):
        # 下载的html源代码
        html = etree.HTML(response.text)
        lis = html.xpath("//ol[@class='grid_view']/li")
        for li in lis:
            # yield 返回一个迭代器，通过next()方法获取元素
            yield DoubanItem({
                "ranking": li.xpath(".//em/text()")[0],  # 排名
                "cover_url": li.xpath(".//img/@src")[0],  # 封面图
                "jump_url": li.xpath(".//div[@class='hd']/a/@href")[0],  # 跳转
                "title": li.xpath(".//span[@class='title']/text()")[0],  # 标题
                "score": li.xpath(".//span[@class='rating_num']/text()")[0]  # 评分
            })
        try:
            # 获取翻页链接信息
            next_page = html.xpath(".//span[@class='next']/a/@href")[0]
            # 手动发送请求下一页数据
            yield scrapy.Request(self.start_urls[0]+next_page,callback = self.parse)
        except:
             print("下载完毕")



