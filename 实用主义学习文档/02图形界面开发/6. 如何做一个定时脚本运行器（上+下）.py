# UI --> UI&User --> UI&User&Core --> B.E.C
# watcher
#
#t -> t_data
#data = [
#    {file_path:123,sart_time:20:00},
#    {file_path:123,sart_time:20:00},
#    {}
#]
from tkinter import *
import threading
import multiprocessing
from runpy import run_path
import time
data = []

def make_app():
    app = Tk()
    app.geometry('300x400')
    Button(name='add',text='add',command=make_task).pack(side=BOTTOM)
    return app

def make_task():
    _font = ['Hack',18,'bold']
    f = Frame(bg='#f2f2f2')
    Label(f,name='lb_name',text='Script name',bg='#f2f2f2',font=_font).pack(anchor='nw')
    Label(f,name='lb_time',text='time',bg='#f2f2f2').pack(side=LEFT)
    Button(f,text=':',command=lambda:make_win(f)).pack(anchor='se')
    f.pack(fill=X)

def make_win(f):
    t = Toplevel(f)
    Label(t,text='FILE PATH').pack()
    Entry(t,name='file_ipt').pack()
    Label(t,text='START TIME').pack()
    Entry(t,name='time_ipt').pack()
    Button(t,text='save',command=lambda:(save(t),t.destroy())).pack()

def save(t):
    d = {}
    file_path  = t.children['file_ipt'].get()
    start_time = t.children['time_ipt'].get()
    d['file_path']  = file_path
    d['start_time'] = start_time
    d['execute'] = False
    data.append(d)
    # [{},{}]

def watcher():
    def _test():
        print(data)

    def _refresh_task():
        # task --> data --> (t -> t_data)
        # [1,2] [a,b] --> 1a 2b ---> zip
        tasks = [t[1] for t in app.children.items() if t[0] != 'add'] #(key,value) children['key'] --> value
        for d,t in zip(data,tasks):
            t.children['lb_name']['text'] = d['file_path']
            t.children['lb_time']['text'] = d['start_time']

    def _task_check():
        now = time.ctime().split()[-2]

        for d in data:
            if d['start_time'] <= now and not d['execute']:
                p = multiprocessing.Process(target=lambda:run_path(d['file_path']))
                # 注意：linux/mac系统下可以使用视频中的lambda表达式，windows系统的用户，需要按此方法调用Process模块。
                # p = multiprocessing.Process(target=run_path, args=(d['file_path'],))
                # 其中，args是target函数中的参数。在windows中，由于不同的系统机制，target不建议使用lambda表达式，很容易产生错误。
                p.start()
                d['execute'] = True


    def _main():
        while True:
            time.sleep(0.5)
            _test()
            _refresh_task()
            _task_check()

    t = threading.Thread(target=_main,name='watcher')
    t.start()

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    app.after(0,watcher)
    app.mainloop()






6. 挑战练习：定时脚本运行器增加运行状态
根据任务的完成状态，该任务的背景色发生变化：
当任务已完成，任务的背景色为浅绿色：#EDFDF1
当任务正在进行中，任务的背景色为浅蓝色：#E9F2FD
当任务未完成，任务的背景色为浅灰色：#F5F7FA
如图：https://video.mugglecode.com/status.png
 
查看提示
•	问题拆解提示
•	在基础题的代码的基础上，添加颜色修改，分为以下若干步骤：
•	1.如何判断程序是尚未执行，还是已经运行完毕？
•	2.如何判断程序是否正在执行中？
•	问题解决提示
•	1.利用data中的execute字段，我们可以很方便的判断：如果为True，说明程序已经执行完毕；如果为False，说明程序尚未执行。
•	2.对于“正在执行”这种状态，data中并没有记录，需要我们通过multiprocessing.active_children()方法来查看进程是否在执行中。
 
查看答案
# coding:utf-8
from tkinter import *
from tkinter.filedialog import *
import threading
import multiprocessing
from runpy import run_path
import time
data = []
# 将每个frame按顺序存储到list中
frame_list = []

def make_app():
    app = Tk()
    app.geometry('600x400')
    Button(name='add',text='add',command=make_task).pack(side=BOTTOM)
    return app

def make_task():
    _font = ['Hack',18,'bold']
    f = Frame(bg='#f2f2f2')
    frame_list.append(f)
    Label(f,name='lb_name',text='Script name',bg='#f2f2f2',font=_font).pack(anchor='nw')
    Label(f,name='lb_time',text='time',bg='#f2f2f2').pack(side=LEFT)
    Button(f,text=':',command=lambda:make_win(f)).pack(anchor='se')
    f.pack(fill=X)

def make_win(f):
    # 检查前面是否存在某个frame没有被设置过
    for x in frame_list:
        if x.children['lb_name']['text'] == 'Script name':
            if x != f:
                t = Toplevel(f)
                Label(t, text='请从第一个空任务开始设置').pack()
                return
            else: break
    t = Toplevel(f)
    file_path = StringVar()
    Label(t,text='FILE PATH').pack()
    Entry(t,name='file_ipt', textvariable=file_path).pack()
    # 添加“select”按钮，其中command绑定了两个方法，一个是打开系统弹窗，一个是保持小窗口始终在最前
    Button(t,text='select',command=lambda:(file_path.set(askopenfilename()),t.wm_attributes("-topmost", 1))).pack()
    Label(t,text='START TIME').pack()
    Entry(t,name='time_ipt').pack()
    Button(t,text='save',command=lambda:(save(t),t.destroy())).pack()

def save(t):
    d = {}
    file_path  = t.children['file_ipt'].get()
    start_time = t.children['time_ipt'].get()
    d['file_path']  = file_path
    d['start_time'] = start_time
    d['execute'] = False
    data.append(d)

def watcher():
    def _test():
        print(data)

    def _refresh_task():
        tasks = [t[1] for t in app.children.items() if t[0] != 'add']
        for d,t in zip(data,tasks):
            t.children['lb_name']['text'] = d['file_path']
            t.children['lb_time']['text'] = d['start_time']
            # 判断程序是否执行完毕
            if d['execute']:
                t['bg'] = '#EDFDF1'
            else:
                t['bg'] = '#F5F7FA'
            # 通过active_children()方法来判断程序是否正在执行
            for ch in multiprocessing.active_children():
                if ch.name == d['file_path']:
                    t['bg'] = '#E9F2FD'
                    break

    def _task_check():
        now = time.ctime().split()[-2]

        for d in data:
            if d['start_time'] <= now and not d['execute']:
                # 注意：linux/mac系统下可以使用视频中的lambda表达式，windows系统的用户，需要按此方法调用Process模块。
                # p = multiprocessing.Process(target=run_path, args=(d['file_path'],))
                # 其中，args是target函数中的参数。在windows中，由于不同的系统机制，target不建议使用lambda表达式，很容易产生错误。
                p = multiprocessing.Process(name=d['file_path'], target=run_path, args=(d['file_path'],))
                p.start()
                d['execute'] = True

    def _main():
        while True:
            time.sleep(0.5)
            _test()
            _refresh_task()
            _task_check()

    t = threading.Thread(target=_main,name='watcher')
    t.start()

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    app.after(0,watcher)
    app.mainloop()





