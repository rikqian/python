import pymysql.cursors
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
    sql1 = """SELECT CONCAT('严重程度: ',CONVERT(b.severity,char)) AS la, COUNT(b.severity) AS
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
    # sqlreRole = """SELECT u.realname as la, COUNT(b.resolvedBy) AS num
    #  FROM zt_bug b LEFT JOIN zt_user u ON b.resolvedBy = u.account
    #   WHERE b.product = %d AND b.deleted = '0' AND b.STATUS = 'resolved'
    #    GROUP BY b.resolvedBy""" % pid

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql1)
            sList1 = cursor.fetchall()
            cursor.execute(sql2)
            sList2 = cursor.fetchall()
            cursor.execute(sql3)
            sList3 = cursor.fetchall()

    finally:
        connection.close()
    L1 = [sList1, sList2, sList3]

    return L1


def getdataline(pid):
    connection = pymysql.connect(host='192.168.51.223', user='test',
                                 password='123456',
                                 db='zentao', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    # 通过information_schema表获取数据库atm6000db_bs中所有的column及table名称

    # 4 近期新增bug曲线 日期 - 等级 -数量
    sqla = """SELECT  DATE(openedDate) as la,CONCAT('严重程度: ',CONVERT(severity,char)) as lb ,COUNT(openedDate) as num FROM zt_bug
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
    connection = pymysql.connect(host='192.168.51.223', user='test',
                                 password='123456',
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


def formatbyPerson(d):
    """
    http://www.pygal.org/en/stable/documentation/types/xy.html
    可以使用pygal.DDateLine,但是x轴坐标的距离会按照时间比例显示，并不对齐
    """
    lalist = sorted(set([x['la'] for x in d]))
    lblist = sorted(set([x['lb'] for x in d]))
    datalist = []
    # ladata = []
    for item in d:
        # print(item)
        datalist.append([item['la'], item['lb'], item['num']])
    return lalist, lblist, datalist


def formatdata(d):
    """列表d有字典组成，字典结构为：{分类1，分类2，数量}
    曲线图中，x轴标签为 分类1
    使用linechart.add("分类2"，数量-列表格式)
    """

    # 获取所有 分类1：日期 的去重列表
    lalist = sorted(set([x['la'] for x in d]))
    # 获取所有 分类2：人员/严重等级 的去重列表
    lblist = sorted(set([x['lb'] for x in d]))
    # 曲线图希望按照分类2生成多条曲线，所以以 分类2 为基准，循环遍历列表d。结果是每个 分类2 对应一个列表，包含分类1的数量，不存在的补0
    ladata = []
    for lb in lblist:
        tempdata = []
        for la in lalist:
            value = 0
            for item in d:
                if (item['la'] == la) & (item['lb'] == lb):
                    value = item['num']
                    break
            tempdata.append(value)
        ladata.append(tempdata)
    return lalist, lblist, ladata


if __name__ == "__main__":
    # d = getdataline(49)[0]
    for d in getdataline(49):
        # date, person, num = formatdata(d)
        date, person, num = formatbyPerson(d)
        print(date)
        print(person)
        print(num)
        # for i, e in enumerate(num):
        #     print(i, e)
