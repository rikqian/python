# Python 3.6, PyMySQL 0.7.10
import pymysql.cursors

ss = "realtime_event(dev_code ,dev_type ,event_type ,"\
    "event_sub_type ,event_data ,is_confirm ,event_detail ,confirm_operator ,"\
    "confirm_detail ,lowmachine_key ,is_sync,event_time) VALUES( "


def sql_generator():
# Set the range of container
    for i in range(1, 271):
        f = "'W2S2C%d' ,400 ,0 ,%d ,NULL ,0 ,'python event detail' ,NULL ,NULL ,NULL ,0 ,DATE_SUB(NOW(),INTERVAL %d MINUTE))" % (
            i, (i % 6), i)
        yield (ss + f)


def createdata():
    connection = pymysql.connect(host='192.168.54.170', user='agioe', password='agioe',
                                 db='atm6000db_yuh_product', charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            for statement in sql_generator():
                cursor.execute('insert into %s' % statement)

            connection.commit()

    finally:
        cursor.close()
        connection.close()

# Set the loop times
for i in range(0, 5):
    createdata()
