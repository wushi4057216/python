import xlrd
import xlwt
from xlutils.copy import copy

tem_execl = xlrd.open_workbook("./日统计.xls", formatting_info=True) #打开xls文件，带表格样式
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
borders.top = xlwt.Borders.THIN #单元格线
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

new_sheet.write(2,1,12,style)
new_sheet.write(3,1,12,style)
new_sheet.write(4,1,12,style)
new_sheet.write(5,1,12,style)

new_execl.save('填写.xls')


