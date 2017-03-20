from copy import deepcopy

# 定义列表a,创建b和a使用同样的对象引用
a = ['test', [1, 2, 3]]
b = a[:]
c = deepcopy(a)

# print(b)


def pid(x):

    for i in [id(n) for n in x]:
        print(i, end='   ')
    print('\n')

# 打印a,b值的地址，ab中所有值的地址相同；
# c中不可变string的地址与a相同，可变类型列表的地址与a不同
pid(a)
pid(b)
pid(c)

# 修改列表a中两个元素的值
a[0] = 'modify'
a[1].append(4)

# 打印a,b值的地址，ab中string的地址不同，列表的地址相同；
# c中不可变string的地址与a相同，可变类型列表的地址与a不同
pid(a)
pid(b)
pid(c)
print(a, b, c)
