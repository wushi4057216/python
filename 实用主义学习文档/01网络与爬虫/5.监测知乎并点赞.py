from selenium import webdriver
import time

# 运行前先下载 chrome driver,下载地址是：https://sites.google.com/a/chromium.org/chromedriver/downloads，点击【Latest Release: ChromeDriver x.xx】进入下载

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver') # Windows 需写成'./chromedriver.exe'
    driver.start_client()
    return driver

def find_strangers():
    # btn
    btn_sel = 'div.ContentItem-extra > button.Button--blue'
    elems = driver.find_elements_by_css_selector(btn_sel)
    return elems

def add_fren():
    pass


while True:
    url = 'https://www.zhihu.com/'
    follower_url = 'https://www.zhihu.com/people/xxx/followers' #需替换成你的知乎url，点击【我的主页】→【关注者】可进入该页面
    driver = start_chrome()
    driver.get(url)
    if not driver.get_cookies():
        push()
    time.sleep(20)
        # wait login

    driver.get(follower_url)
    time.sleep(6) # wait for loading page & users
    strangers = find_strangers()
    for s in strangers:
        s.click()
        time.sleep(3)
    print('Done!')
    time.sleep(3000)
# js_execute('xxx.click()')
