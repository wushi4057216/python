#修改原有表格内容并另存
from xlutils.copy import copy
import xlrd

tem_execl = xlrd.open_workbook('日统计.xls')
new_execl = copy(tem_execl)

new_sheet = new_execl.get_sheet(0)
new_sheet.write(2, 1, 44)   #写入值(行,列,内容)
new_sheet.write(3, 1, 55)

new_execl.save('日统计.xls')

#创建新xls文件的方法
import xlwt
new_workbook = xlwt.Workbook()
workbook = new_workbook.add_sheet("日统计")    #创建新工作簿
workbook.write(0,0,"test")  #写入内容(行,列,内容)
new_workbook.save('d:/test.xls')



