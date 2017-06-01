import pymysql.cursors
import itertools
# import datetime
# import re


def getdata(pid):
    # 数据库连接
    connection = pymysql.connect(host='192.168.51.223', user='test',
                                 password='123456',
                                 db='zentao', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    # 通过information_schema表获取数据库atm6000db_bs中所有的column及table名称

    # 1 未解决BUG按严重程度
    sql1 = """SELECT CONCAT('严重程度：',b.severity) AS la, COUNT(b.severity) AS
     num FROM zt_bug b WHERE b.product = %d AND b.deleted = '0' AND b.STATUS = 'active'
      GROUP BY b.severity""" % pid

    # 2 未解决按指派对象
    sql2 = """SELECT u.realname as la, COUNT(b.assignedTo) AS num
     FROM zt_bug b LEFT JOIN zt_user u ON b.assignedTo = u.account
      WHERE b.product = %d AND b.deleted = '0' AND b.STATUS = 'active'
       GROUP BY b.assignedTo""" % pid

    # 3 已解决按解决方案分类
    sql3 = """SELECT resolution as la,COUNT(resolution) AS num FROM zt_bug
     WHERE product = %d AND deleted = '0' AND STATUS = 'resolved '
      GROUP BY resolution""" % pid

    # 已解决按解决者分类
    sqlreRole = """SELECT u.realname as la, COUNT(b.resolvedBy) AS num
     FROM zt_bug b LEFT JOIN zt_user u ON b.resolvedBy = u.account
      WHERE b.product = %d AND b.deleted = '0' AND b.STATUS = 'resolved'
       GROUP BY b.resolvedBy""" % pid

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql1)
            sList1 = cursor.fetchall()
            # result1 = [(row[0], row[1]) for row in cursor.fetchall()]
            cursor.execute(sql2)
            sList2 = cursor.fetchall()
            cursor.execute(sql3)
            sList3 = cursor.fetchall()
            # cursor.execute(sql1)
            # sList0 = cursor.fetchall()

            # result2 = ((row[0], row[1]) for row in cursor.fetchall())

            # cursor.execute(sqlreRole)
            # result3 = ((row[0], row[1]) for row in cursor.fetchall())

    finally:
        connection.close()
    L1 = [sList1, sList2, sList3]

    return L1
# for r in cursor.fetchall():
# 	print(r['num'])
# print(sList1)
# print(type(sList1))
# result1.__next__()
# print(next(result3))


def getdataline(pid):
    connection = pymysql.connect(host='192.168.51.223', user='test',
                                 password='123456',
                                 db='zentao', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    # 通过information_schema表获取数据库atm6000db_bs中所有的column及table名称

    # 4 近期新增bug曲线 日期 - 等级 -数量
    sqla = """SELECT  DATE(openedDate) as la,CONCAT('严重程度：',severity) as lb ,COUNT(openedDate) as num FROM zt_bug
     WHERE product = %d AND deleted = '0' AND openedDate > DATE_SUB(CURDATE(), INTERVAL 10 DAY)
      GROUP BY DATE(openedDate),severity""" % pid

    # 5 近期新增bug曲线 日期 - 人员 -数量
    sqlb = """SELECT  DATE(openedDate) as la,(SELECT u.realname FROM zt_user u WHERE u.account = openedby) as lb,COUNT(openedDate) as num FROM zt_bug
     WHERE product = %d AND deleted = '0' AND openedDate > DATE_SUB(CURDATE(), INTERVAL 10 DAY)
      GROUP BY DATE(openedDate),openedby """ % pid
    try:
        with connection.cursor() as cursor:
            cursor.execute(sqla)
            sList4 = cursor.fetchall()
            cursor.execute(sqlb)
            sList5 = cursor.fetchall()
    finally:
        connection.close()

    L2 = [sList4, sList5]
    return L2


def getpid():
    connection = pymysql.connect(host='192.168.57.10', user='root',
                                 password='ajdts',
                                 db='zentao', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    sql = "SELECT id,name FROM zt_product WHERE status = 'normal' and code like 'ATM6000%'"
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            plist = cursor.fetchall()

    finally:
        connection.close()

    return plist


if __name__ == "__main__":
    # l1,l2,l3 = getdata()
    # # print(len(l2))
    # # print(l1,l2,l3)
    # pat = '.*?－{1}(.*)'
    # for r in [x['la'] for x in l1]:
    # 	# print(r)
    # 	print(re.search(pat,r))
    # l = getpid()
    # for item in l:
    #     print(item['id'], item['name'])
    testlist = getdataline(49)[0]
    newlist = []
    LL = []
    for item in testlist:
        newlist.append([i for i in item.values()])
    # for item in newlist:
    #     print(item)
    # print(type(newlist[0][0]), type(newlist[0][1]), type(newlist[0][2]))
    severity = list(set([i['lb'] for i in testlist]))
    print(severity)
    # print(type(severity[0]))
    date = sorted(list(set([i['la'] for i in testlist])))
    print(date)
    # print(type(date[0]))
    for s in severity:
        for d in date:
            t = 0
            for item in newlist:
                if (item[1] == s) & (item[0] == d):
                    t = item[2]
                    break
            LL.append(t)

    # for item in LL:
    #     print(item)
    print(LL[0:28])
    print(LL[0:8])

    # severity = set([i['lb'] for i in testlist])
    # date = set([i['la'] for i in testlist])
    # for s, d in severity, date:
    #     for it in testlist:
    #     	if it[s]
    # grouplist = itertools.groupby(newlist, lambda item: item[1])
    # for g, v in grouplist:
    #     print(g, list(v))
