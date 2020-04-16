from bs4 import BeautifulSoup
import requests
import xlrd,xlwt
'''运行报错，需检查代码配置'''
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('housedata')
worksheet.write(0, 0, '标题')
worksheet.write(0, 1, '位置')
worksheet.write(0, 2, '装修')
worksheet.write(0, 3, '楼层')
worksheet.write(0, 4, '租金')
worksheet.write(0, 5, '户型')
worksheet.write(0, 6, '发布时间')

n = 1
for i in range(1,11):
    url = 'https://hf.lianjia.com/zufang/'.format(i)
    web_data = requests.get(url).text.encode('latin1').decode('utf-8')
    print(web_data)
    soup = BeautifulSoup(web_data, 'lxml')
    titles = soup.select('tr > td.subject > a.subject_t')
    places = soup.select('tr > td.subject > div')
    prices = soup.select('tr > td.nth-of-type(2)')
    areas = soup.select('tr > td:nth-of-type(3)')
    times = soup.select('tr > td:nth-of-type(4)')

    for title, place, price, area, add_time in zip(titles, places, prices, areas, times):
        title_clean = title.get_text().replace('\t', '').replace('\n', '').replace('\xa0', '').replace('\r', '')
        place_clean = place.get_text().replace('\t', '').replace('\n', '').replace('\xa0', '').replace('\r', '')
        price_clean = price.get_text().replace('\t', '').replace('\n', '').replace('\xa0', '').replace('\r', '')
        area_clean = area.get_text().replace('\t', '').replace('\n', '').replace('\xa0', '').replace('\r', '')
        time_clean = add_time.get_text().replace('\t', '').replace('\n', '').replace('\xa0', '').replace('\r', '')

        headline = title_clean
        location = place_clean[0:place_clean.find('[')]
        fitment = place_clean[place_clean.find(']') + 1:place_clean.find('/') - 1 ]
        level = place_clean[place_clean.find('/') - 1:]
        rental = price_clean
        house_type = area_clean
        pubdate = time_clean

        worksheet.write(n, 0, headline)
        worksheet.write(n, 1, location)
        worksheet.write(n, 2, fitment)
        worksheet.write(n, 3, level)
        worksheet.write(n, 4, rental)
        worksheet.write(n, 5, house_type)
        worksheet.write(n, 6, pubdate)
        n += 1

new_workbook.save('houst_data.xls')