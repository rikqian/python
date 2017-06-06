import dbinfo


def ping(addr):
    import os
    ostype = os.name
    if ostype == 'nt':
        r = os.system("ping -n 1 %s" % addr)
    elif ostype == 'posix':
        r = os.system("ping -c 1 %s" % addr)
    if r == 0:
        status = True
    else:
        status = False
    # print(ostype)
    # print(status)
    # print(status)
    return status


if __name__ == '__main__':
    # import os
    import datetime
    fname = 'REPORT_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.log'
    fobj = open(fname, 'w')
    env = dbinfo.getenv()
    fobj.writelines("------ 环境主机链接状况 ------\n")
    for item in env[0]:
        # print("%s  ip: %s,connection status: %s" %
        #       (item['name'], item['ip'], ping(item['ip'])))
        fobj.writelines("%s  ip: %s,connection status: %s\n" %
                        (item['name'], item['ip'], ping(item['ip'])))
    fobj.writelines("\n\n\n------ 环境ACU链接状况 ------\n")
    for item in env[1]:
        # print("%s  ip: %s, connection status: %s" %
        #       (item['name'], item['ip'], ping(item['ip'])))
        fobj.writelines("%s  ip: %s, connection status: %s\n" %
                        (item['name'], item['ip'], ping(item['ip'])))
    acumaddr = [acum['ip'] for acum in env[0]]
    # print(acumaddr)
    kvtabledata = dbinfo.getkvtable(acumaddr)
    # print(kvtabledata)
    fobj.writelines('\n\n\n------ 未配置lowermachinekey的环境采集器 ------\n')
    # print('NO configuration for devices:')
    for item in env[2]:
        fobj.writelines("设备编号: %s, 属性: %s\n" %
                        (item['name'], item['property']))
        # print("devcode: %s, property: %s" % (item['name'], item['property']))
    fobj.writelines('\n\n\n------ 无效lowermachinekey的环境采集器 ------\n')
    # print('ENV device with invalid lowmachine_key:')
    for item in env[3]:
        if not(item['key'] in kvtabledata):
            fobj.writelines("设备编号: %s, 属性: %s, 下位机关键字: %s\n" %
                            (item['name'], item['property'], item['key']))
    cable = dbinfo.getcable()
    fobj.writelines('\n\n\n------ 电缆主机链接状况 ------\n')
    for item in cable[0]:
        fobj.writelines("%s  ip: %s, connection status: %s\n" %
                        (item['name'], item['ip'], ping(item['ip'])))
    fobj.writelines('\n\n\n------ 电缆采集器链接状况 ------\n')
    for item in cable[1]:
        fobj.writelines("%s  ip: %s, connection status: %s\n" % (item['name'], item['ip'],
                                                                 ping(item['ip'])))
