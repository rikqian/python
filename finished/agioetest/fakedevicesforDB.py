import pymysql
import datetime
connection = pymysql.connect(host='192.168.57.10', user='root',
                             password='ajdts',
                             db='atm6000db_v22_base', charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


def gen(n):
    """
    创造假数据：普通照明设备
    """
    list = []
    # date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # date = datetime.datetime(2017, 3, 31, 0, 0, 50)
    dev_type = 212
    dev_model = '普通照明'

    sql = """INSERT INTO atm6000db_v22_base.env_device_info
    (dev_code, dev_name, dev_type, dev_model, pipegalley_code, part_code, gis_coordinate,
    panorama_key)
    VALUES
    ('fakeZM%d', 'fake照明%d', %d, '%s', 'T2', 'T2P2', '(0:0)', '0');"""
    for i in range(100, 100 + n):
        list.append(sql % (i, i, dev_type, dev_model))
    return list


def genSeg():
    list = []
    sql = """INSERT INTO atm6000db_v22_base.cable_segment_detail_info (seg_code, cable_core_type,
     phase_code, start_location, end_location, cable_type_code, hot_parameter_code, lay_condition_code,
     update_time, current_flag) values
     (3000100+%d,1,)"""


data = gen(151)

try:
    with connection.cursor() as cursor:
        for item in data:
            cursor.execute(item)
        connection.commit()
finally:
    cursor.close()
    connection.close()
