import urllib
import requests,time
from lxml import etree


url = {#"http://zrzyt.ah.gov.cn",   #可以使用
      # "http://zrzyt.ah.gov.cn/zd/pqxxgk/index.jsp",   #可以使用
      # "http://112.122.8.3:8887/ah",   #可以使用
     #  "http://112.122.8.3:9661/xtjs/login.jsp",   #看不到源码
       #"http://112.122.8.4:88/gtxt/public/xyda/list",  #可以使用
   #404    "http://www.ahtd.org.cn/",
    #404     "http://www.ahgtcj.org.cn/",
 #可以使用      "http://ch.ah.gov.cn/",
    #404      "http://www.ahgm.org.cn/",
 #报错      "http://www.ahshkzy.com/",
    #可以使用      "http://zrzy.bengbu.gov.cn/",
    #看不到源码       "http://ah.tianditu.gov.cn/",
    #报错     "60.173.22.133/mobile_sl.html",
    #报错      "60.173.22.133/mobile_zs.html",
    #看不到源码      "http://zrzyghj.xuancheng.gov.cn/"
       }
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Cache-Control': 'max-age=0',
          'Connection': 'keep-alive',
          'Cookie': 'JSESSIONID=aaawhaVAL8Fe7fTJ3qUWw; path=/; HttpOnly',
          'Host': 'zrzyt.ah.gov.cn',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
          'Upgrade-Insecure-Requests': '1'
          }
for i in url:
    html = requests.get(url=i, headers=header).text
    print(i)
    #查找指定文字内容
    ah = html.find('的')
    print(ah)
    print(html)
    #检查xgag字段信息
 #   etree_html = etree.HTML(html)
 #   content = etree_html.xpath('/html/body/div[4]/div/div[1]/div/a[5]/text()')
 #   PRINT(CONTENT)
 #   for each in content:
 #       print(each)
