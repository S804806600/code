from selenium import webdriver
from selenium.webdriver import ChromeOptions
import xlwt

option = ChromeOptions()
# 不显示浏览器界面
option.add_argument('--headless')
option.add_argument('--disable-gpu')

print('开始爬取数据')
driver = webdriver.Chrome(options=option)
driver.get(url='https://www.aliexpress.com/wholesale?SearchText=hat')
js = 'return window.runParams.mods.itemList.content' # js语句
result=driver.execute_script(js) # 获取执行js的结果


# 创建excel表并设置表头
workbook=xlwt.Workbook(encoding='utf-8')
booksheet=workbook.add_sheet('商品', cell_overwrite_ok=True)
row = ["商品名称","图片url","售价","评分","销量"]
for i in range(0, len(row)):
    booksheet.write(0, i, row[i])

print('数据处理中')
index=0
for i in result:
    index+=1
    try:
        booksheet.write(index, 0, i['title']['displayTitle'])
        booksheet.write(index, 1, i['image']['imgUrl'])
        booksheet.write(index, 2, i['prices']['salePrice']['minPrice'])
        booksheet.write(index, 3, i['evaluation']['starRating'])
        booksheet.write(index, 4, i['trade']['tradeDesc'])
    except:
        continue

workbook.save('商品数据.xls')
print('处理结束')

