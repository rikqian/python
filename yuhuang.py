import pymysql.cursors

ss = "insert into realtime_event(dev_code ,dev_type ,event_type ,"\
    "event_sub_type ,event_data ,is_confirm ,event_detail ,confirm_operator ,"\
    "confirm_detail ,lowmachine_key ,is_sync,event_time) VALUES"


def sql_generator():

    for i in range(1, 3):
        f = "('W2S2C%d' ,400 ,0 ,%d ,NULL ,0 ,'python event detail' ,NULL ,NULL ,NULL ,0 ,'DATE_SUB(NOW(),INTERVAL %d MINUTE)'')" % (
            i, (i % 6), i)
        yield f


def sql_generator2():
    for i in range(51, 52):
        f = ''''W1S1C1%s' ,400 ,0 ,%d ,10 ,0 ,'python event detail' ,NULL ,NULL ,NULL ,0 ,DATE_SUB(NOW(),INTERVAL %d MINUTE))''' % (
            i, (i % 6), i)
    yield f


'''generator test'''
for item in sql_generator():
    print(item)
    print(type(item))


def createdata():
    connection = pymysql.connect(host='192.168.54.170', user='agioe', password='agioe',
                                 db='atm6000db_yuh_product', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # sql = r"select * from privilege_type"
            # cursor.execute(sql)

            # Method 1: Use the executemandy to loop###

            # sql = '%s'
            cursor.executemany(ss+"%s", sql_generator())
            # for content in sql_generator():
            #     print(sql % content)

            # Method 2: Use the FOR loop to insert many reocrds###
            # for statement in sql_generator():
            #     cursor.execute('insert into %s' % statement)

            # connection.commit()

    finally:
        cursor.close()
        connection.close()


for i in range(0, 1):
    createdata()
