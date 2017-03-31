import pymysql.cursors
import datetime

# obsoleting
# ss = "insert into realtime_event(dev_code ,dev_type ,event_type ,"\
#     "event_sub_type ,event_data ,is_confirm ,event_detail ,confirm_operator ,"\
#     "confirm_detail ,lowmachine_key ,is_sync,event_time) VALUES"

# obsoleting
# def sql_generator():

#     for i in range(1, 3):
#         f = "('W2S2C%d' ,400 ,0 ,%d ,NULL ,0 ,'python event detail' ,NULL ,NULL ,NULL ,0 ,'DATE_SUB(NOW(),INTERVAL %d MINUTE)')" % (
#             i, (i % 6), i)
#         yield f

# obsoleting
# def sql_generator2():
#     for i in range(51, 52):
#         f = ''''W1S1C1%s' ,400 ,0 ,%d ,10 ,0 ,'python event detail' ,NULL ,NULL ,NULL ,0 ,DATE_SUB(NOW(),INTERVAL %d MINUTE))''' % (
#             i, (i % 6), i)
#     yield f


def sql_gen():
    for i in range(1, 201):
        f = (i, (i % 6), i)
        yield f


def sql_gen1():
    d = datetime.datetime(2017, 3, 31, 0, 0, 50)
    for i in range(1, 201):
        f = (i, (i % 6), d)
        yield f

sql =  "insert into realtime_event(dev_code ,dev_type ,event_type ,"\
    "event_sub_type ,event_data ,is_confirm ,event_detail ,confirm_operator ,"\
    "confirm_detail ,lowmachine_key ,is_sync,event_time) VALUES"\
    "('W2S2C%s' ,400 ,0 ,%s ,NULL ,0 ,'python event detail' ,NULL ,NULL ,NULL ,0 ,DATE_SUB(NOW(),INTERVAL %s MINUTE))"

sql1 =  "insert into realtime_event(dev_code ,dev_type ,event_type ,"\
    "event_sub_type ,event_data ,is_confirm ,event_detail ,confirm_operator ,"\
    "confirm_detail ,lowmachine_key ,is_sync,event_time) VALUES"\
    "('W2S2C%s' ,400 ,0 ,%s ,NULL ,0 ,'python event detail' ,NULL ,NULL ,NULL ,0 ,%s)"


'''generator test'''
# for item in sql_generator():
#     print(item)
#     print(type(item))


def createdata():
    connection = pymysql.connect(host='localhost', port=3309, user='root', password='123456',
                                 db='atm6000db_yuh', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:

            # cursor.executemany(sql, sql_gen())
            cursor.executemany(sql1, sql_gen1())

            # Method 2: Use the FOR loop to insert many reocrds###
            # for statement in sql_gen():
            #     cursor.execute(sql % statement)

            connection.commit()
    finally:
        cursor.close()
        connection.close()


def getdata():
    connection = pymysql.connect(host='localhost', port=3309, user='root', password='123456',
                                 db='atm6000db_yuh', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    query = "select * from realtime_event order by update_time desc limit 1"
    querycount = "select count(*) from realtime_event"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)

            # connection.commit()
            print(cursor.fetchall())
            cursor.execute(querycount)
            print(cursor.fetchall())
    finally:
        cursor.close()
        connection.close()


# execution
# for i in range(0, 101):
#     createdata()

# getdata()
