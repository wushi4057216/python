# coding:utf-8
import csv
import time
from wxpy import *

# 将要发送的好友的名字存到list中
FRIENDS = ['王总','麻瓜编程君','沫沫']
CSV_PATH = './MeetingMsg.csv'

# 定义函数获取csv中的内容
def read_csv(path):
    f = open(path, 'r')
    reader = csv.DictReader(f)
    return [info for info in reader]

# 定义获取发送内容的函数
def get_msg(infos, name):
    template = "{name}，提醒下，{time}记得来参加{event}，地点在{location}，{note}"
    for info in infos:
        if info['微信昵称'] == name:
            msg = template.format(
                name = info['微信昵称'],
                time = info['时间'],
                event = info['事件'],
                location = info['地址'],
                note = info['备注']
            )
            return msg
    # 如果在infos列表中没有找到对应的微信昵称，则输出None
    return None

# 定义用于群发操作的函数
def send_to_friends(infos, friends):
    # 初始化微信机器人
    bot = Bot()
    for friend in friends:
        # 搜素好友
        try:  #新增的异常处理
            friend_search = bot.friends().search(friend)
        except ResponseError as e:
            print(e.err_code, e.err_msg)
        # 如果搜索结果仅有一个，则发送图片，否则返回错误信息
        if (len(friend_search) == 1):
            msg = get_msg(infos, friend)
            if not msg:
                try:  #新增的异常处理
                    friend_search[0].send(get_msg(infos, friend))
                except ResponseError as e:
                    print(e.err_code, e.err_msg)
            else:
                print("发送失败！用户名不在csv中："+friend)
        else:
            print("发送失败！请检查用户名："+friend)
        time.sleep(3)

# 调用群发函数
send_to_friends(read_csv(CSV_PATH), FRIENDS)
