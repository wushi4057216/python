import xlrd
import xlwt
from xlutils.copy import copy

xlsx = xlrd.open_workbook('7月下旬入库表.xls')

table = xlsx.sheet_by_index(0)

#循环获取表格内数据保存到临时字典
all_data = []
for n in range(1,table.nrows):
    company = table.cell(n,1).value
    price = table.cell(n,2).value
    weight = table.cell(n,3).value

    data = {'company':company, 'price':price, 'weight':weight}
    all_data.append(data)

a_weight = []
a_total_price = []
b_weight = []
b_total_price = []
c_weight = []
c_total_price = []

for i in all_data:
    if i['company'] == '张三粮配':
        a_weight.append(i['weight'])
        a_total_price.append(i['weight'] * i['price'])
    if i['company'] == '李四粮食':
        a_weight.append(i['weight'])
        a_total_price.append(i['weight'] * i['price'])
    if i['company'] == '王五小麦':
        a_weight.append(i['weight'])
        a_total_price.append(i['weight'] * i['price'])
    if i['company'] == '赵六麦子专营':
        a_weight.append(i['weight'])
        a_total_price.append(i['weight'] * i['price'])

tem_execl = xlrd.open_workbook('统计表_模板.xls', formatting_info=True)
tem_sheet = tem_execl.sheet_by_index(0)

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

new_sheet.write(2,1,len(a_weight), style)
new_sheet.write(2,2,round(sum(a_weight), 2), style) #round保留小数点2位
new_sheet.write(2,3,round(sum(a_total_price), 2), style)
new_sheet.write(3,1,len(a_weight), style)
new_sheet.write(3,2,round(sum(a_weight), 2), style)
new_sheet.write(3,3,round(sum(a_total_price), 2), style)
new_sheet.write(4,1,len(a_weight), style)
new_sheet.write(4,2,round(sum(a_weight), 2), style)
new_sheet.write(4,3,round(sum(a_total_price), 2), style)
new_sheet.write(5,1,len(a_weight), style)
new_sheet.write(5,2,round(sum(a_weight), 2), style)
new_sheet.write(5,3,round(sum(a_total_price), 2), style)

new_execl.save('./7月下旬统计表.xls')










