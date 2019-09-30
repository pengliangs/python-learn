from lxml import etree

# 创建元素
html = etree.Element("html")
head = etree.Element("head")
body = etree.Element("body")
div = etree.Element("div")
body.append(div)
head.append(body)
html.append(head)
print(etree.tostring(html, pretty_print = True).decode())
