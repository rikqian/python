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
    for i in range(0, n):
        list.append(sql % (i, i, dev_type, dev_model))
    return list


# for item in gen(10):
#     print(item)
# print(datetime.datetime.now())
# print(datetime.datetime.now().isoformat(timespec='seconds'))
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
data = gen(1)

try:
    with connection.cursor() as cursor:
        for item in data:
            cursor.execute(item)
        connection.commit()
finally:
    cursor.close()
    connection.close()
