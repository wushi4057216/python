import asyncio
from pyppeteer import launch
import time

from pyppeteer.browser import Browser



async def main():
    url = {"http://zrzyt.ah.gov.cn",  # 可以使用
           "http://zrzyt.ah.gov.cn/zd/pqxxgk/index.jsp",  # 可以使用
           "http://112.122.8.3:8887/ah",  # 可以使用
           "http://112.122.8.3:9661/xtjs/login.jsp",  # 看不到源码
           "http://112.122.8.4:88/gtxt/public/xyda/list",  # 可以使用
           "http://www.ahtd.org.cn/",  # 404
           # 404     "http://www.ahgtcj.org.cn/",
           "http://ch.ah.gov.cn/",  # 可以使用
           # 404      "http://www.ahgm.org.cn/",
           # 报错      "http://www.ahshkzy.com/",
           "http://zrzy.bengbu.gov.cn/",  # 可以使用
           # 看不到源码       "http://ah.tianditu.gov.cn/",
           # 报错     "60.173.22.133/mobile_sl.html",
           # 报错      "60.173.22.133/mobile_zs.html",
           # 看不到源码      "http://zrzyghj.xuancheng.gov.cn/"
           }
    name = (1,2,3,4,5,6,7,8,9,10)
    name = str(name)
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    for url in url:
        await page.goto(url)
#    await page.type("#Login_Name_Input", "test02")
#    await page.type("#Login_Password_Input", "12345678", )
      #  await asyncio.sleep(100)
        await page.screenshot({'path':name+'.png'})
 #   await page.click("#Login_Login_Btn")
  #      await page.close()
  #  await browser.close()
  #  await page.waitFor(1000)




asyncio.get_event_loop().run_until_complete(main())