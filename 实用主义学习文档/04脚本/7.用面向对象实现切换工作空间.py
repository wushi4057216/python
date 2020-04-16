# Windows版代码
from sconfig import CONFIGS
import os
import win32gui
import win32api
import win32con

class WorkSpace:

    def __init__(self, c):
        self.folders = c['folders']
        self.name    = c['name']
        self.target  = c['target']
        # 添加两个新的字段
        self.wallpaper = c['wallpaper']
        self.softwares = c['softwares']

    def switch(self):
        for f in os.listdir(self.target):
            if f.endswith('.wspc'):
                path = self.target + f
                os.remove(path)
        # Step1：创建快捷方式
        # 以下部分是 Windows 系统的写法，其他代码一致。另外由于 windows 系统运行 MKLINK 需要管理员权限，推荐使用 cmder 运行 http://www.jeffjade.com/2016/01/13/2016-01-13-windows-software-cmder/，或者用管理员身份打开cmd，然后运行python script_lesson_7_mac.py.
        for source in self.folders:
            real_target = self.target + source.split('\\')[-1] + '.wspc'
            command = ['MKLINK', '/D', real_target, source]
            # WINDOWS下使用os.system
            os.system(' '.join(command))

        # Step2：根据CONFIG中的内容，配置壁纸
        self.change_wallpaper(self.wallpaper)

        # Step3：根据CONFIG中的内容，打开指定软件
        for software in self.softwares:
            self.open_software(software)

    # Windows下自动打开软件
    def open_software(self, software):
        software = r"C:\Windows\System32\notepad.exe"
        os.startfile(software)

    # Windows下自动切换壁纸
    def change_wallpaper(self, wallpaper):
        wallpaper = r"D:\MuggleCoding\脚本练习题7\life.jpg"
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
            "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        # 拉伸适应桌面
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        # 桌面居中
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, wallpaper, 1+2)

workspaces = [WorkSpace(c) for c in CONFIGS]
print('Choose your workspace:')
choice = input()
for w in workspaces:
    if w.name == choice:
        w.switch()

# 以下是WINDOWS下的sconfig.py文件
CONFIGS = [
    {
        'name':'WORK',
        'folders':[
            # source
            'D:\\Codes\\Java',
            'D:\\Codes\\Python'
        ],
        # 指定壁纸的绝对路径
        'wallpaper':'D:\\MuggleCoding\\脚本练习题7\\work.jpg',
        # 需要指定APP的绝对路径，如C:\Users\Administrator\Desktop\Pycharm.exe
        'softwares':[
            'pycharm.exe',
            'evernote.exe'
        ],
        # where
        'target':'C:\\Users\\Administrator\\Desktop\\'
    },

    {
        'name': 'PLAY',
        'folders':[
            # source
            'D:\\myfiles\\video',
            'D:\\myfiles\\game'
        ],
        'wallpaper':'D:\\MuggleCoding\\脚本练习题7\\life.jpg',
        'softwares':[
            'chrome.exe',
            'wechat.exe'
        ],
        # where
        'target':'C:\\Users\\Administrator\\Desktop\\'
    },

]

# Mac版代码
from subprocess import call
import os
from sconfig import CONFIGS
import os

CONFIGS = [
    {
        'name':'WORK',
        'folders':[
            # source
            '/Codes/Java',
            '/Codes/Python'
        ],
        # 指定壁纸的绝对路径
        'wallpaper':'/MuggleCoding/脚本练习题7/work.jpg',
        # 需要指定APP的绝对路径，如C:\Users\Administrator\Desktop\Pycharm.exe
        'softwares':[
            'pycharm.app',
            'evernote.app'
        ],
        # where
        'target':'/Users/Administrator/Desktop/'
    },

    {
        'name': 'PLAY',
        'folders':[
            # source
            '/myfiles/video',
            '/myfiles/game'
        ],
        'wallpaper':'/MuggleCoding/脚本练习题7/life.jpg',

        'softwares':[
            # In MacOS all applications' executable path is under the ROOT dir '/Applications'
            # '/Applications/WeChat.app'
            # '/Applications/Chrome.app'
            'chrome.app',
            'wechat.app'

        ],
        # where
        'target':'/Users/Administrator/Desktop/'
    },

]


class WorkSpace:

    def __init__(self, c):
        self.folders = c['folders']
        self.name    = c['name']
        self.target  = c['target']
        # 添加两个新的字段
        self.wallpaper = c['wallpaper']
        self.softwares = c['softwares']

    def switch(self):
        for f in os.listdir(self.target):
            if f.endswith('.wspc'):
                path = self.target + f
                os.remove(path)
        # Step1：创建快捷方式
        for source in self.folders:
            real_target = self.target + source.split('/')[-1] + '.wspc'
            command = ['ln', '-s', source, real_target]
            # python -m xxx.py
            call(command)

        # Step2：根据CONFIG中的内容，配置壁纸
        self.change_wallpaper(self.wallpaper)

        # Step3：根据CONFIG中的内容，打开指定软件
        for software in self.softwares:
            self.open_software(software)

    # Mac下自动打开软件
    def open_software(self, software_path):
        command = ["open", software_path]
        call(command)

    # Mac下自动切换壁纸，调用Finder应用
    def change_wallpaper(self, wallpaper_path):
        # First: brew install wallpaper (A wallpaper commandline tool)
        # Usage: wallpaper /full/path/to/example.jpg
        command = ['wallpaper', wallpaper_path]
        call(command)

workspaces = [WorkSpace(c) for c in CONFIGS]
print('Choose your workspace:')
choice = input()
for w in workspaces:
    if w.name == choice:
        w.switch()
