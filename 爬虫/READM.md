# robots协议

访问淘宝 https://www.taobao.com/robots.txt

```text
User-agent:  Baiduspider
Allow:  /article
Allow:  /oshtml
Allow:  /ershou
Allow: /$
Disallow:  /product/
Disallow:  /

User-Agent:  Googlebot
Allow:  /article
Allow:  /oshtml
Allow:  /product
Allow:  /spu
Allow:  /dianpu
Allow:  /oversea
Allow:  /list
Allow:  /ershou
Allow: /$
Disallow:  /
....

User-Agent:  *
Disallow:  /
```
User-agent ： 用户信息
Allow：允许搜索爬取目录
Disallow：不允许搜索爬取目录

User-Agent:* 其他用户

马蜂窝 https://www.mafengwo.cn/robots.txt

```text
.....

User-agent: *
Disallow: /
Disallow: /poi/detail.php

Sitemap: http://www.mafengwo.cn/sitemapIndex.xml
```
Sitemap 官网地图，将所有的允许爬去内容汇总这样就不让你去网站到处找了

robots 是一个君子协议，这个协议是为了让搜索引擎更有效的搜索自己的内容，提供了如 Sitemap 这样的文件

