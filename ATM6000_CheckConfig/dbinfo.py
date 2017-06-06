import pymysql.cursors
import urllib.request
import re
# connection = pymysql.connect(host='192.168.51.113', user='root',
#                              password='ajdts',
#                              db='atm6000db_bs', charset='utf8',
#                              cursorclass=pymysql.cursors.DictCursor)


def dbinfo():
    # import os
    result = {}
    with open('dbconfig.ini') as file:
        for eachline in file:
            line = eachline.strip('\n')
            result[(line.split('='))[0]] = (line.split('='))[1]
    print('Database information: %s ' % result)
    return result


dbbb = dbinfo()


def getenv():
    db = dbbb
    connection = pymysql.connect(host=db['host'], user=db['user'],
                                 password=db['password'],
                                 db=db['database'], charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    sqlacum = "select mname as name,mip as ip from env_acum_info"
    sqlacu = "select acu_name as name,acu_ip as ip from env_acu_info"
    # valid lowermachine key devices exclude: 230 , 233, 231
    sqlenvdev_no = """select dev_code as name, property_key as property from env_realtimedata where lowmachine_key = ''"""
    sqlenvdev = """SELECT dev_code AS name, property_key AS property, lowmachine_key AS `key` FROM env_realtimedata WHERE lowmachine_key != '' AND dev_type NOT IN (230,233,251) AND property_key NOT IN ('Alarm_state','RelationCtrlBox','LinkageDevCode') AND property_key NOT LIKE '%LevelAlarm'"""
    with connection.cursor() as cursor:
        cursor.execute(sqlacum)
        acuminfo = cursor.fetchall()
        cursor.execute(sqlacu)
        acuinfo = cursor.fetchall()
        cursor.execute(sqlenvdev_no)
        dev_no = cursor.fetchall()
        cursor.execute(sqlenvdev)
        dev = cursor.fetchall()
    return acuminfo, acuinfo, dev_no, dev


def getcable():
    db = dbbb
    connection = pymysql.connect(host=db['host'], user=db['user'],
                                 password=db['password'],
                                 db=db['database'], charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    sqlmachine = "select machine_name as name,ip_addr as ip from machine_info"
    sqlcollector = "select collector_name as name,ip_addr as ip from collector_info"
    with connection.cursor() as cursor:
        cursor.execute(sqlmachine)
        machineinfo = cursor.fetchall()
        cursor.execute(sqlcollector)
        collectorinfo = cursor.fetchall()

    return machineinfo, collectorinfo


def getkvtable(acumaddr):
    # http://192.168.57.222/cgi-bin/control.cgi?cmd=create_kv_table&func=control
    data = []
    for addr in acumaddr:
        genurl = 'http://' + addr + \
            '/cgi-bin/control.cgi?cmd=create_kv_table&func=control'
        tableurl = 'http://%s/KVTable.txt' % addr
        # print(genurl)
        # print(tableurl)
        urllib.request.urlopen(genurl)
        with urllib.request.urlopen(tableurl) as response:
            table = response.read().decode('utf-8')
        data.extend(re.compile('\d{8}').findall(table))
        # print(data)
    return data
    # print(type(table))
    # for item in talbe:


if __name__ == '__main__':
    # print(getacum())
    # import os
    # status = os.system('ping -n 1 192.168.57.222')
    # print(status)
    # if status == 0:
    #     print('OK')
    # else:
    #     print('Not')
    # getkvtable(['192.168.57.222'])
    getenv()
