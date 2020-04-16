# coding:utf-8
import os
import shutil
# 需要把路径替换成你的文件夹所在路径，当把这个代码文件放在要处理的文件夹外一层时，可以使用下面的相对路径写法
path = './problem2_files'
# 创建目标文件夹
os.makedirs(path + '/image')
os.makedirs(path + '/document')
# 将需要处理的后缀名存储到list中
image_suffix = ['jpg', 'png', 'gif']
doc_suffix = ['doc', 'docx', 'ppt', 'md']
# 移动jpg、png、gif文件中的文件
for i in image_suffix:
    cur_path = path + '/' + i
    files = os.listdir(cur_path)
    for f in files:
        # 移动文件夹中的文件
        shutil.move(cur_path + '/' + f, path + '/image')
    # 删除文件夹
    os.removedirs(cur_path)
# 移动doc、docx、md、ppt文件夹中的文件，步骤与前面类似
for d in doc_suffix:
    cur_path = path + '/' + d
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(cur_path + '/' + f, path + '/document')
    os.removedirs(cur_path)
