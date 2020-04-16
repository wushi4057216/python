# Core --> Core&UI --> Core&UI&User --> Boundary.Edge.Corner
# app app2
#  ||  \\

import time
from tkinter import *
from multiprocessing import Process
import threading

info = {
    'total_time':60
}

def make_app():
    _font = ['Hack',25,'bold']
    app = Tk()
    Label(name='lb',text=0,font=_font).pack()
    Button(name='btn',text='start',command=time_counts).pack()
    Entry(name='ipt').pack()
    app.geometry('150x75')
    return app

def time_counts():
    def _counts():
        while info['total_time']:
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)

    t = threading.Thread(target=_counts,name='timer')
    t.start()

def ui_watcher():

    def _update_button():
        btn = app.children['btn']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if timer:
            btn['state'] = 'disabled' # 'disabled'
        else:
            btn['state'] = 'normal'

    def _get_time():
        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if not timer and ipt.get():
            info['total_time'] = int(ipt.get())

    def _update_time():
        lb = app.children['lb']
        lb['text'] = info['total_time']

    def _main():
        while True:
            #_update_button()
            print("I'm watching you")
            print(threading.enumerate())
            _get_time()
            _update_time()
            _update_button()
            time.sleep(0.5)

    t = threading.Thread(target=_main,name='watcher')
    t.start()

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    #app.after(0,time_counts)
    app.after(0,ui_watcher)
    app.mainloop()



5. 挑战练习：倒计时小工具的停止功能
在课程代码基础上补全开始按钮的逻辑：
①当倒计时运行时，开始按钮变成停止按钮。点击时停止倒计时。如图：https://video.mugglecode.com/stop.png
②当倒计时停止时，按钮为开始按钮。
 
查看提示
•	问题拆解提示
•	与更新按钮状态类似，该问题需要修改按钮的text属性和command属性，以完成“开始”->“停止”文字上的转换，以及功能上的转换。拆解为如下若干步骤：
•	1.修改text属性
•	2.修改command属性
•	3.编写停止倒计时的函数
•	问题解决提示
•	1.通过btn['text']修改text属性
•	2.通过btn['command']修改command属性
•	3.通过修改info['total_time']，使其为0，来达到停止倒计时的效果。
 
查看答案
# coding:utf-8
import time
from tkinter import *
import threading

info = {
    'total_time':60
}

def make_app():
    _font = ['Hack',25,'bold']
    app = Tk()
    Label(name='lb',text=0,font=_font).pack()
    Button(name='btn',text='开始',command=time_counts).pack()
    Entry(name='ipt').pack()
    app.geometry('150x100')
    return app

def time_counts():
    def _counts():
        while info['total_time']:
            info['total_time'] -= 1
            print(info['total_time'])
            time.sleep(1)

    t = threading.Thread(target=_counts,name='timer')
    t.start()
# 通过修改total_time的值，来完成停止操作
def time_stop():
    info['total_time'] = 0

def ui_watcher():
    # 将input框禁用的函数
    def _update_input():
        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        ipt['state'] = 'disabled' if timer else 'normal'
    # 修改按钮状态的函数
    def _update_button():
        btn = app.children['btn']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        btn['text'] = '停止' if timer else '开始'
        btn['command'] = time_stop if timer else time_counts

    def _get_time():
        ipt = app.children['ipt']
        timer = [t for t in threading.enumerate() if t.name == 'timer']
        if not timer and ipt.get():
            info['total_time'] = int(ipt.get())

    def _update_time():
        lb = app.children['lb']
        lb['text'] = info['total_time']

    def _main():
        while True:
            #_update_button()
            print("I'm watching you")
            print(threading.enumerate())
            _get_time()
            _update_time()
            _update_button()
            _update_input()
            time.sleep(0.5)

    t = threading.Thread(target=_main,name='watcher')
    t.start()

app = make_app()
app.after(0,ui_watcher)
app.mainloop()








