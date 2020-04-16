import  xlrd

xlsx = xlrd.open_workbook('7月下旬入库表.xlsx')
table = xlsx.sheet_by_index(0)#表许路号
#table = xlsx.sheet_by_name('7月下旬入库表')
#根据行列读取内容
print(table.cell_value(1,1))
print(table.cell(1,2).value)
print(table.row(1)[3].value)


# for n in range(1,table.nrows):
#     print(table.cell_value(n,1))
#     print(table.cell_value(n,2))
#     print(table.cell_value(n,3))

