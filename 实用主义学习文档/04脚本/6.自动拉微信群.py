# coding:utf-8
import time
from wxpy import *

# 通过群名找到群聊
def find_group(bot, name):
    try:
        result = bot.groups().search(name)
        if len(result) == 1:
            return result[0]
        else:
            print("监测失败！未发现群或存在多个名称相同的群。")
            return None
    except ResponseError as e:
        print(e.err_code, e.err_msg)
# 获取群聊的成员列表
def get_members(group):
    try:
        return group.members
    except ResponseError as e:
        print(e.err_code, e.err_msg)
# 对比新旧两个成员列表
def parse_members(cur_members, last_members):
    # 获取退群名单：如果旧成员不在新的成员列表中，说明他退群了
    quit_list = [last.name for last in last_members if last not in cur_members]
    # 获取进群名单：如果新成员不在旧的成员列表中，说明他是新加群的
    new_list = [cur.name for cur in cur_members if cur not in last_members]
    # 返回文本信息
    return "退群名单："+"，".join(quit_list)+"\n"+"进群名单："+"，".join(new_list)
# 将指定的消息发送给指定的人
def send_msg(bot, my_name, text):
    try:
        myself = bot.friends().search(my_name)[0]
        myself.send(text)
    except ResponseError as e:
        print(e.err_code, e.err_msg)
# 将主要操作封装在main函数中
def main(my_name, group_name):
    bot = Bot()
    group = find_group(bot, group_name)
    # 先获取一次成员列表，便于后续对比
    last_members = get_members(group)
    # 利用while True和sleep，实现每隔1小时进行一次监测
    while True:
        time.sleep(3600)
        # 获取当前的成员列表
        cur_members = get_members(group)
        msg = parse_members(cur_members, last_members)
        send_msg(bot, my_name, msg)
        # 将当前成员列表赋值给last_members变量，当作下一次操作中的旧成员列表
        last_members = cur_members
# 调用main函数，执行监测
main("我自己的微信名","群名称")
