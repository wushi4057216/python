from tkinter import *
import os

app = Tk()
label = Label(text='All hidden files',font=('Hack',25,'bold')) #Hack是自己安装的字体，如果你没安装，可以用系统自带的Arial字体
label.pack()
listbox = Listbox(bg='#f2f2f2',fg='red')
listbox.pack(fill=BOTH,expand=True)
path = '/Users/cybermaster/' #这里需要换成你的路径
files = os.listdir(path)
for f in files:
    if f.startswith('.'):
        listbox.insert(END,f)

app.mainloop()
#app.run()
