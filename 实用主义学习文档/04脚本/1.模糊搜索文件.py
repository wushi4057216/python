import os
path = 'd:/'
# path这里应该替换成你的路径，Windows 用户的桌面文件夹路径是类似这样的：C:/Users/yourusername/Desktop/images
files = os.listdir(path)
#print(files)

for f in files:
    if f.endswith('.exe') and 'Docker' in f:
        print('Look! I found this   ' + f)
