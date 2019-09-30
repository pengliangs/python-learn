from urllib import parse
import ssl
from urllib.request import urlopen, Request

# url编码解码
url = "https://cn.bing.com/search";
param = {
    "q": "美女"
}
encode_param = parse.urlencode(param)
base_usr = "%s?%s" % (url, encode_param)

print("base_usr", base_usr)
print("urlencode", encode_param)
print("unquote", parse.unquote(encode_param))

# 忽略https不信任证书
context = ssl._create_unverified_context();

# 请求对象
req = Request(base_usr, headers={
    # 用户头信息，模拟一个浏览器
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/77.0.3865.90 Safari/537.36"
})

# 打开统一资源定位地址 url，可以是一个字符串或一个 Request 对象。

with urlopen(req,context = context) as res:
    with open("bing_mm.html","wb+") as file_obj:
        file_obj.write(res.read())
        file_obj.flush()
