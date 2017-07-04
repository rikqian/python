def calA(n):
    ''' 护套环流计算公式g_Var1*(ADVal/g_Var2 * g_Var3)+g_Var4)*(g_Var5/g_Var6);
    但是当使用该公式时，主机给ATM6000发送的护套环流值为整形。导致客户端运算时会
    将采集数据转换为整形再按照公式计算。
    '''
    print(1.958 * (n / 1024 * 5) * 100 / 5)


if __name__ == "__main__":
    calA(25)
    calA(27)
    calA(26)
