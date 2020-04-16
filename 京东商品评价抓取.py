import requests
import re,json
from requests.exceptions import HTTPError,Timeout,RequestException,ProxyError,ConnectTimeout
from concurrent.futures import ThreadPoolExecutor
import csv,pymysql,threading


class JdSpider(object):
    """" step2: 定义一个类JdSpider，完成爬虫主体代码 在__init__初始化方法中添加相关属性"""
    def __init__(self, start_url):
        """
        :param start_url: 商品url地址
        """
        # 设置商品url地址
        self.start_url = start_url

        # 创建csv文件
        self.csv_file = open('jd.csv', 'a+')
        # csv文件头部用户头像headerUrl、用户昵称nickName、星级startLevel、内容content、产品信息productInfo、评论图片地址commentImages、评论视频地址videoUrl、发布时间publishTime。
        fileNames = ['headerUrl', 'nickName', 'startLevel', 'content', 'productInfo', 'commentImages', 'videoUrl',
                     'publishTime', ]
        # 创建csv文件句柄
        self.writer = csv.DictWriter(self.csv_file, fieldnames=fileNames)
        # 写入csv文件头部
        self.writer.writeheader()

        # 创建数据库链接
        self.mysql_client = pymysql.Connect(
            host='192.168.3.131', user='root', password = 'redhat',
            database='jd', port=3306, charset='utf8'
        )
        # 创建游标
        self.cursor = self.mysql_client.cursor()

        # 实例化一个lock（互斥锁）
        self.myLock = threading.Lock()

        self.start_request(self.start_url)

    def start_request(self, start_url):
        """step3: start_request ：根据商品url地址发起请求获取响应结果，提取商品的id以及能获取的最大页码数量，拼接商品评论url地址，并将所有请求任务添加进线程池。"""
        # 获取商品的id
        # match：根据正则表达式，从字符串中提取符合正则表达式的结果，
        # 从起始位置开始匹配，如果不符合正则规则，直接返回None，单次
        # 匹配

        # search：根据正则表达式，从字符串中提取符合正则表达式的结果
        # 从整个字符串中匹配符合正则规则的子串，有结果直接返回，否则返回
        # None，单次匹配
        # https://item.jd.com/100000177760.html#comment
        prodect_id = re.search('\d+', start_url).group()
        firstComUrl = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv193&productId=%s&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1" % prodect_id
        response_text = self.send_request(firstComUrl)
        if response_text:
            # print('获取到了数据',response_text)
            json_data = json.loads(response_text)
            # 获取能请求评论的最大页码数量
            maxPage = int(json_data['maxPage'])
            print('能够获取的最大页码数量', maxPage)
            # 将任务添加线程池中
            pool = ThreadPoolExecutor(10)
            for page in range(maxPage):
                comUrl = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv193&productId=%s&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1" % (
                prodect_id, str(page))
                result = pool.submit(self.send_request, comUrl)
                print(result)
                result.add_done_callback(self.parse_comments)
            pool.shutdown()

    def send_request(self, url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}):
        """"step4: send_request该方法根据url地址使用requests发送请求，返回请求的响应结果"""
        try:
            response = requests.get(url, headers=headers, timeout=10)
            print(response)
            if response.status_code == 200:
                print('请求成功', response.status_code)
                return response.text
        except (HTTPError, Timeout, RequestException, ProxyError, ConnectTimeout) as err:
            print(err)
            return None

    def parse_comments(self, future):
        """""step5: parse_comments解析商品评论接口返回的评论数据，注意这里返回的是一个json字符串，需要使用json.loads将json字符串转换为python数据类型然后取值"""
        response_text = future.result()
        print(response_text)
        if response_text:
            # 解析数据
            comments = json.loads(response_text)['comments']
            print(comments)
            for comment in comments:
                commentInfo = {}
                # 姓名
                commentInfo['nickName'] = comment['nickname']
                # 内容
                commentInfo['content'] = comment['content']
                # 其他数据依次获取,给你们留点写代码的机会


                # 存储数据
                self.save_db_to_csv(commentInfo)
                self.save_db_to_db(commentInfo)

    def save_db_to_csv(self, commentInfo):
        # 将数据写入csv文件
        self.myLock.acquire()
        self.writer.writerow(commentInfo)
        self.myLock.release()

    def save_db_to_db(self, commentInfo):
        # 将数据写入数据库

        sql = """
        INSERT INTO jingdong (%s)
        VALUES (%s)
        """ % (','.join(commentInfo.keys()), ','.join(['%s'] * len(commentInfo)))
        print(sql, list(commentInfo.values()))
        # python中线程安全，
        # 加锁
        print(self.myLock)
        self.myLock.acquire()
        try:
            self.cursor.execute(sql, list(commentInfo.values()))
            self.mysql_client.commit()
            print('插入数据成功')
        except Exception as err:
            self.mysql_client.rollback()
            print(err)
        # 解锁
        self.myLock.release()

if __name__ == "__main__":
    start_url = 'https://item.jd.com/52269577755.html'
    jdSpider = JdSpider(start_url)



"""""使用有异常,查询不到评价内容"""