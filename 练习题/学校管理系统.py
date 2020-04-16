print("="*50)
print("  学校管理系统")
print("1.添加人员")
print("2.查询")
print("3.改名")
print("4.退出")
print("="*50)

names = []


while True:
    nums = int(input("请输入操作码"))
    if nums==1:
        num = input("请输入人名")
        names.append(num)
    elif nums==2:
        num = input("请输入人名")
        if num in names:
            print("查到此人")
        else:
            print("查无此人")
    elif nums==3:
        num = input("请输入要改的人名")
        if num in names:
            names.remove(num)
            num = input("请输入修改新名字")
            names.append(num)

            print(names)
    elif nums==4:
        break
    else:
        print("输入错误")