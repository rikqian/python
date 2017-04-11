# Python 3.6, PyMySQL 0.7.10， beautifulsoup4 4.5.3
import pymysql.cursors
import urllib.request
from bs4 import BeautifulSoup

# 从mysql官网爬去所有保留字,并生成列表
def getReserved():
	url = 'https://dev.mysql.com/doc/refman/5.5/en/keywords.html' # mysql5.5版本 官网关键字保留字网页url
	# url = "file:///E:/git/python/localtest/Reserved%20Words.htm"
	with urllib.request.urlopen(url) as response:
		doc = response.read()

	soup = BeautifulSoup(doc,"html.parser")
	# print(soup.prettify())

	target = soup.find(id="table-keywords-5.5-detailed") # 按照页面元素table的id找到关键字保留字列表
	target2 = target.tbody # 仅查找第一个tbody内容，第二个列表内容为注释内容，没有用

	tdlist = target2.find_all("td") # 使用find_all生成所有td标签项的列表

	reservedwords = [] #新建空列表
	for item in tdlist:
		# print(item)
		if "(R)" in str(item) and item.code != None: # 通过是否有包含(R)字符串来判断保留字
			# print(item.code.string)
			reservedwords.append(item.code.string) # 将所有查出的保留字添加到列表

	return reservedwords



# 数据库连接
connection = pymysql.connect(host='192.168.57.102', user='root',
                             password='ajdts',
                             db='information_schema', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
# 通过information_schema表获取数据库atm6000db_bs中所有的column及table名称
sql = "SELECT column_name,table_name FROM COLUMNS WHERE table_schema = 'atm6000db_v22_base'" 
sqltable = "SELECT DISTINCT(table_name) FROM COLUMNS WHERE table_schema = 'atm6000db_v22_base'"
reservedlist = getReserved()
try:
    with connection.cursor() as cursor:
        cursor.execute(sql)

    print("###字段名与保留字重复###")
    print('-列名-','    -表名-')
    for i in cursor.fetchall():
    	# print(i['column_name'])

        # 判断列名称是否与保留字重复
        # sql执行结果为一个字典元素组成的列表，所以要查询字典键值来匹配
        if i['column_name'].upper() in reservedlist:
            print(i['column_name'],i['table_name'])

finally:
    cursor.close()
    # connection.close()


try:
    with connection.cursor() as cursor1:
        cursor1.execute(sqltable)

    print("\n###表名与保留字重复###")
    print(r'-表名-')
    for x in cursor1.fetchall():

        # 判断列名称是否与保留字重复
    	if x['table_name'].upper() in reservedlist:		
    		print(x['table_name'])


finally:
    cursor1.close()
    connection.close()
