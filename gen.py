# 生成器

longestline = max(len(line.strip()) for line in open('file.py'))
# print(longestline)


class A(object):

    def __init__(self, i):
        from time import sleep, time
        sleep(i)
        print(time())


print([A(i) for i in range(5)])

# for x in (A(i) for i in range(5)):
#     print(x)
