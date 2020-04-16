from runpy import run_path
from tkinter import *
#from multiprocessing import Process
import multiprocessing
import os
# app exe  --> id --> pid
# |script| --> func1 --> fun2 --> func3 ...
# \App\ --> display() & {if do()} --> update() & {if do()}

def make_app():
    app = Tk()
    Listbox(name='listb').pack()
    Button(text='run',command=run_script).pack()
    Button(text='stop',command=stop_script).pack()
    return app

def ui_make_list():
    listb = app.children['listb']
    for d in os.listdir():
        listb.insert(END,d)

def run_script():
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    p = multiprocessing.Process(name='print',target=lambda :run_path(s_path))
    # 注意：linux/mac系统下可以使用视频中的lambda表达式，windows系统的用户，需要按此方法调用Process模块。
    # p = multiprocessing.Process(name='print', target=run_path, args=(s_path,))
    # 其中，args是target函数中的参数。在windows中，由于不同的系统机制，target不建议使用lambda表达式，很容易产生错误。
    p.start()

def stop_script():
    for p in multiprocessing.active_children():
        if p.name == 'print':
            p.terminate()

def watcher():
    print(multiprocessing.active_children())
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    print(s_path)
    app.after(1000,watcher)

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    app.after(100,ui_make_list)
    app.after(0,watcher)
app.mainloop()

4. 挑战练习：脚本运行工具的交互优化
① 在课程代码基础上增加一个 open 按钮，能弹出系统弹窗选择任意路径的文件，然后将文件移动到这个项目代码所在的 GUI 文件目录列表中，并且在程序界面的 listbox 中显示了这个文件。
② 当某个程序运行结束的时候，在界面上这个任务的这一行显示 √。如图：https://video.mugglecode.com/done.png








from runpy import run_path
from tkinter import *
#from multiprocessing import Process
import multiprocessing
import os
# app exe  --> id --> pid
# |script| --> func1 --> fun2 --> func3 ...
# \App\ --> display() & {if do()} --> update() & {if do()}

def make_app():
    app = Tk()
    Listbox(name='listb').pack()
    Button(text='run',command=run_script).pack()
    Button(text='stop',command=stop_script).pack()
    return app

def ui_make_list():
    listb = app.children['listb']
    for d in os.listdir():
        listb.insert(END,d)

def run_script():
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    p = multiprocessing.Process(name='print',target=lambda :run_path(s_path))
    # 注意：linux/mac系统下可以使用视频中的lambda表达式，windows系统的用户，需要按此方法调用Process模块。
    # p = multiprocessing.Process(name='print', target=run_path, args=(s_path,))
    # 其中，args是target函数中的参数。在windows中，由于不同的系统机制，target不建议使用lambda表达式，很容易产生错误。
    p.start()

def stop_script():
    for p in multiprocessing.active_children():
        if p.name == 'print':
            p.terminate()

def watcher():
    print(multiprocessing.active_children())
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    print(s_path)
    app.after(1000,watcher)

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    app.after(100,ui_make_list)
    app.after(0,watcher)
    app.mainloop() 


查看提示
•	问题拆解提示
•	该问题可以拆解为如下若干子问题：
•	1.如何弹出选择文件的窗口？
•	2.如何将选择好的文件移动到./gui路径下？
•	3.如何判断一个程序是否运行结束？
•	问题解决提示
•	1.利用tkinter.filedialog模块中的askopenfilenames函数，实现打开选择文件窗口的操作。
•	2.参考【脚本】第一阶段中所学到的shutil模块，其中的move函数提供了移动文件的功能。需要指定文件所在路径和目标路径。
•	3.利用MultiProcessing库中Process对象的is_alive()方法，来检查一个进程是否已经执行完毕。并且利用两个list来记录，一个list叫running，当启动一个进程的时候，将它放入running中；另一个list叫have_done，每隔一段时间检查running中的每个进程，如果is not alive，则认为该进程已经运行完毕，将其放入have_done中。
 
查看答案
# coding:utf-8
from runpy import run_path
from tkinter import *
from tkinter.filedialog import *
import multiprocessing
import shutil
import os

# 用于存放正在运行的进程
running = []
# 用于存放已经运行完毕的进程
have_done = []

# 创建GUI框体
def make_app():
    app = Tk()
    Listbox(app, name='listb').pack(fill=BOTH, expand=True)
    Button(app, text='open', command=openfile).pack()
    Button(app, text='run', command=run_script).pack()
    Button(app, text='stop', command=stop_script).pack()
    app.geometry('300x400')
    return app

# 填充listbox，并监测正在运行的程序是否已经运行完毕
def ui_make_list():
    # 获取listbox，以便修改其内容
    listb = app.children['listb']
    # 清空listbox中的内容
    listb.delete(0,END)
    for d in os.listdir('./gui'):
        # 如果一个进程已经运行完毕，则显示√
        listb.insert(END,d) if d not in have_done else listb.insert(END, d+'            √')

# open按钮的功能：打开系统弹窗选择文件，并将这些文件移动到./gui目录下
def openfile():
    f_names = askopenfilenames()
    for f in f_names:
        shutil.move(f, './gui')
    ui_make_list()

# 运行脚本文件
def run_script():
    # 获取listbox
    listb = app.children['listb']
    # 获取listbox中当前点击的的元素
    s_path = listb.get(ACTIVE)
    # 检查需要run的脚本是否已经在运行
    for child in multiprocessing.active_children():
        # 如果已经在运行，则输出信息，并退出函数
        if child.name == s_path:
            print("This script is already running.")
            return
    # 如果未运行，则创建新的进程来运行它。
    # 注意此处target和args。args是target函数需要的参数。
    # linux/mac系统下可以使用视频中的lambda表达式，windows系统下需要按此方法使用，该方法是更标准的一种方法。
    p = multiprocessing.Process(name=s_path, target=run_path, args=('./gui/'+s_path,))
    p.start()
    running.append(p)

# 停止脚本运行
def stop_script():
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    for p in multiprocessing.active_children():
        if p.name == s_path:
            p.terminate()
            return
    print("This script is not running.")

# 监测程序状态
def watcher():
    # 利用MultiProcessing库中Process对象的is_alive()方法，来检查一个进程是否已经执行完毕
    for r in running:
        if not r.is_alive() and r.name not in have_done:
            have_done.append(r.name)
            ui_make_list()
    print(multiprocessing.active_children())
    listb = app.children['listb']
    s_path = listb.get(ACTIVE)
    print(s_path)
    app.after(1000, watcher)

# 注意，在windows系统下，必须按此方法执行。linux/mac系统可以不要if这句话。
if __name__ == '__main__':
    app = make_app()
    app.after(100, ui_make_list)
    app.after(0, watcher)
app.mainloop()





