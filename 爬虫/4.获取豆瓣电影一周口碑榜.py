from lxml import etree
import requests

url = "https://movie.douban.com/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/77.0.3865.90 Safari/537.36"

with requests.get(url,headers={"User-Agent":user_agent}) as res:
    # html 内容
    content = res.text

    # 解析html
    html = etree.HTML(content)

    # 解析元素
    trs = html.xpath("//div[@class='billboard-bd']//tr")

    for tr in trs:
        # print(etree.tostring(tr, pretty_print = True).decode())
        order = tr.xpath(".//td[@class='order']/text()")
        title = tr.xpath(".//td[@class='title']//text()")
        print(f"order={order[0]},title={title[0]}")
