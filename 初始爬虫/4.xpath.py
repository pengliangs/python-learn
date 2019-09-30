from lxml import etree

html_str = """
<div>
    <ul>
        <li class="item"><a href="one.html">one item</a></li>
        <li class="item"><a href="two.html">two item</a></li>
        <li class="item"><a href="three.html">three item</a></li>
        <li class="item"><a href="four.html">four item</a></li>
        <li class="item"><a href="five.html" id="five">five item</a></li>
    </ul>
</div>
"""

# 默认会将html字符转换为标准html格式
html = etree.HTML(html_str)
# print(etree.tostring(html, pretty_print = True).decode())

# 使用xpath获取解点文本内容,默认返回列表
print(html.xpath("/html/body/div/ul/li/a/text()"))

# https://www.w3school.com.cn/xpath/index.asp
# / 从根节点选取。
# // 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
print(html.xpath("//a/text()"))
# 获取属性 /@属性名称
print(html.xpath("//a/@href"))
# 根据属性匹配
print(html.xpath("//a[@id='five']/@href"))