# coding:utf-8
import os
import filecmp

# 需要把路径替换成你的文件夹所在路径，当把这个代码文件放在要处理的文件夹外一层时，可以使用下面的相对路径写法
path = './problem3_files'
# 已知路径下存在两个文件夹pic1和pic2
dirs = ['pic1','pic2']

# 将指定目录下的所有文件的路径存储到all_files变量中
def get_all_files(path, dirs):
    all_files = []
    for d in dirs:
        cur_path = path + '/' + d
        files = os.listdir(cur_path)
        for f in files:
            all_files.append(cur_path + '/' + f)
    return all_files

# 比较两个文件的内容是否一致
def cmp_files(x, y):
    if filecmp.cmp(x, y):
        # 如果一致，则删除第二个，保留第一个，并输出信息
        os.remove(y)
        print("路径\"" + y + "\"下的文件是重复文件，已经删除")

# 调用函数，获取文件列表
all_files = get_all_files(path, dirs)
# 用双重for循环来比较文件是否有重复
for x in all_files:
    for y in all_files:
        # 如果x和y不是相同的文件，而且都存在，则执行后续操作
        if x != y and os.path.exists(x) and os.path.exists(y):
            # 比较两个文件的内容是否一致
           cmp_files(x,y)
