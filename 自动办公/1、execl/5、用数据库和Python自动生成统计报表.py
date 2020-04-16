import xlrd
import xlwt
import pymysql
from xlutils.copy import copy

database = pymysql.Connect("127.0.0.1", "test", "test", "db", charset='utf8')

cursor = database.cursor()

sql = "select company, COUNT(company), SUM(weight), SUM(weight*price) from data group by company"
cursor.execute(sql)
result = cursor.fetchall()
#print(result)
for i in result:
    if i[0] == "张三粮配":
        a_num = i[1]
        a_weighi = i[2]
        a_total_price = i[3]
    elif i[0] == "李四粮食":
        a_num = i[1]
        a_weighi = i[2]
        a_total_price = i[3]
    elif i[0] == "王五小麦":
        a_num = i[1]
        a_weighi = i[2]
        a_total_price = i[3]
    elif i[0] == "赵六麦子专营":
        a_num = i[1]
        a_weighi = i[2]
        a_total_price = i[3]

tem_execl = xlrd.open_workbook("./统计表模板.xls", formatting_info=True) #打开xls文件
tem_sheet = tem_execl.sheet_by_index(0) #读取第一个表

new_execl = copy(tem_execl)
new_sheet = new_execl.get_sheet(0)

style = xlwt.XFStyle()

#设置文字字体
font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360
style.font = font

borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN #单元格线
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

new_sheet.write(2,1,a_num, style)
new_sheet.write(2,2,a_weighi, style)
new_sheet.write(2,3,a_total_price, style)
new_sheet.write(3,1,a_num, style)
new_sheet.write(3,2,a_weighi, style)
new_sheet.write(3,3,a_total_price, style)
new_sheet.write(4,1,a_num, style)
new_sheet.write(4,2,a_weighi, style)
new_sheet.write(4,3,a_total_price, style)
new_sheet.write(5,1,a_num, style)
new_sheet.write(5,2,a_weighi, style)
new_sheet.write(5,3,a_total_price, style)

new_execl.save('./7月下旬统计表.xls')










