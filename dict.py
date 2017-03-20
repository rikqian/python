a = {"name":'earth','port':80}
print(a)
#使用工厂方法dict()创建字典
b = dict((['x',1],['y',2]))
print(b)
#内建方法fromkeys() 创建一个默认字典，字典中的元素具有相同的值.
#如果没用给出，默认为None
d = {}.fromkeys(['x','y'],-1)
print(d)

for key in d:
	print('key=%s, value=%s'%(key,d[key]))