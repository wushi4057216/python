from urllib import parse
from urllib.request import Request,urlopen
##url的编码解码
d = {
    'q':'马哥教育'
}
u = parse.urlencode({'q':'马哥教育'})#编码

url = 'https://cn.bing.com/search?{}'.format(u)

print(url)

print('中'.encode('utf-8'))#编码

print(parse.unquote(url))#解码

ua =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"

req = Request(url,headers={'User-agent':ua})
res = urlopen(req)
print(res)
with res:
    with open('d:/123.html','wb+') as f:
        f.write(res.read())

