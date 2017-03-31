# -*- coding: utf-8 -*-
# Generator Test
import pymysql.cursors
connection = pymysql.connect(host='192.168.54.170', user='agioe',
                             password='agioe',
                             db='atm6000db_bs', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


def gen():
    s = "* from privilege_type where privilege_code = %d"
    for i in range(0, 2):
        yield s % i


def gen2():
    for i in range(0, 2):
        yield i


# for content in gen():
#     print(content)
list = []
for i in range(0, 3):
    list = list + \
        [r" * from privilege_type where privilege_code = '%s'" % i]

# for l in list:
#     print(l)


try:
    with connection.cursor() as cursor:

        # for content in gen():
        #     cursor.execute((content))
        #     print(content)
        sql = "select * from privilege_type where privilege_code = %s"
        cursor.executemany('select %s', gen())
        # cursor.executemany("select * from privilege_type where privilege_code = '%s'" , [0])
        # cursor.execute(
        #     "select * from privilege_type where privilege_code = '0'")
        # cursor.execute(
        #     "select * from privilege_type where privilege_code = '1'")

    connection.commit()
    print(cursor.fetchall())

    # print(cursor.)


finally:
    cursor.close()
    connection.close()
