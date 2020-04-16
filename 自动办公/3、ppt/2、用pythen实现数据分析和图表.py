#from pptx import Presentation
#from pptx.util import Inches,Pt
#安装使用pip install matplotlib
import matplotlib.pyplot as plt
#pip install matplotlib
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签

date = ['2018/7/21', '2018/7/22', '2018/7/23', '2018/7/24', '2018/7/25', '2018/7/26', '2018/7/27', '2018/7/28', '2018/7/29',
        '2018/7/30', '2018/7/31']
hebei = [69, 93, 65, 66, 64, 70, 88, 47, 58, 21,24]
shanxi = [36, 38, 41, 38, 37, 58, 19, 32, 12, 21]

####折线图####
plt.plot(date, hebei, color='red', label= '河北')
plt.plot(date, shanxi, color='blue', label='山西')
plt.title('每日入库量对比')
plt.xlabel('日期')
plt.ylabel('车次')

plt.legend()
plt.show()

####柱状图####
plt.bar(date, hebei, color='red', label='河北')

plt.legend()
plt.show()

####水平柱状图####
plt.barh(date, shanxi, color='blue', lable='山西')

plt.legend()
plt.show()

####饼图####
number = [666, 343]
province = ['河北', '山西']
colors = ['#999fff', '#fff999']

plt.pie(x=number, labels=province, colors=colors)
plt.legend()
plt.show()

#ppt.save('test.pptx')























