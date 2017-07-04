import pymysql
import datetime
connection = pymysql.connect(host='192.168.57.10', user='root',
                             password='ajdts',
                             db='atm6000db_v22_base', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


def gen(n):
    """
    创造假的实时报警事件
    """
    list = []

    sql = """INSERT INTO env_realtimeevent (dev_code,dev_type,property_key,event_type,event_sub_type,\
    event_data,is_confirm,event_detail,confirm_operator,\
    confirm_detail,confirm_time,lowmachine_key, is_sync,event_time,update_time) values\
     ('fakeZM%s',212,'Run_state',0,0,0,0,'Fake Events DB Insert','',\
    '' ,TIMESTAMP(NOW()),'fakelowmachinekey', 0,TIMESTAMP(NOW()),TIMESTAMP(NOW()))"""
    for i in range(0, n):
        list.append(sql % i)
    return list


data = gen(1)

try:
    with connection.cursor() as cursor:
        pass
        # for item in data:
        #     cursor.execute(item)
        # connection.commit()
finally:
    cursor.close()
    connection.close()

print(data)
