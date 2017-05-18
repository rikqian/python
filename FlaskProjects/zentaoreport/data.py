import pymysql.cursors
import re

def getdata():
# 数据库连接
	connection = pymysql.connect(host='192.168.57.17', user='root',
	                             password='ajdts',
	                             db='zentao', charset='utf8',
	                             cursorclass=pymysql.cursors.DictCursor)
	# 通过information_schema表获取数据库atm6000db_bs中所有的column及table名称

	# 未解决按指派对象
	sqlunRole = r"SELECT u.realname as la, COUNT(b.assignedTo) AS num FROM zt_bug b LEFT JOIN zt_user u ON b.assignedTo = u.account WHERE b.product = 49 AND b.deleted = '0' AND b.STATUS = 'active' GROUP BY b.assignedTo"
	 
	# 已解决按解决方案分类

	sqlre = "SELECT resolution as la,COUNT(resolution) AS num FROM zt_bug WHERE product = 49 AND deleted = '0' AND STATUS = 'resolved ' GROUP BY resolution"

	# 已解决按解决者分类
	sqlreRole = "SELECT u.realname as la, COUNT(b.resolvedBy) AS num FROM zt_bug b LEFT JOIN zt_user u ON b.resolvedBy = u.account WHERE b.product = 49 AND b.deleted = '0' AND b.STATUS = 'resolved' GROUP BY b.resolvedBy"


	try:
	    with connection.cursor() as cursor:
		    cursor.execute(sqlunRole)
		    sList1 = cursor.fetchall()
		        # result1 = [(row[0], row[1]) for row in cursor.fetchall()]
		    cursor.execute(sqlre)
		    sList2 = cursor.fetchall()
		    cursor.execute(sqlreRole)
		    sList3 = cursor.fetchall()
		        # result2 = ((row[0], row[1]) for row in cursor.fetchall())

		        # cursor.execute(sqlreRole)
		        # result3 = ((row[0], row[1]) for row in cursor.fetchall())

	finally:
	    connection.close()

	return sList1,sList2,sList3
# for r in cursor.fetchall():
# 	print(r['num'])
# print(sList1)
# print(type(sList1))
# result1.__next__()
# print(next(result3))

if __name__ == "__main__":
	l1,l2,l3 = getdata()
	# print(len(l2))
	# print(l1,l2,l3)
	pat = '.*?－{1}(.*)'
	for r in [x['la'] for x in l1]:
		# print(r)
		print(re.search(pat,r))