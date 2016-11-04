import urllib.request
import random

#  访问该网站可以查看自己当前ip
url = "http://www.whatismyip.com.tw"

#  代理ip列表
iplist = ["121.193.143.249:80","122.96.59.107:843","122.193.14.106:82","122.228.179.178:80"]

#  随机选取代理ip列表中的代理ip
proxy_support = urllib.request.ProxyHandler({"http":random.choice(iplist)})

#  生成open，并添加header
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36")]

#  安装opener包
urllib.request.install_opener(opener)

#  获得返回的二进制数据
response = opener.open(url)

#  读取二进制数据并解码为utf-8编码
html = response.read().decode("utf-8")

print(html)
