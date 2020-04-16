from urllib.request import Request,urlopen
import random
from urllib import parse
#打开一个url返回一个Request请求 对象
url = 'http://www.biqukan.com/1_1094/'

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"
]
ua = random.choice(ua_list)

request = Request(url)
request.add_header('User-agent', ua)
print(type(request))

response = urlopen(request,timeout=5)
print(type(response))

with response:
    print(1,response.status,response.getcode,response.reason)
    print(2,response.geturl())
    print(3,response.info())
   # print(4,response.read())
    aaa = response.read()
    print(4,aaa)
    print(str(parse.unquote(aaa)))  # 解码
print(5,request.get_header('User-agent'))
print(6,'user-agent'.capitalize())


