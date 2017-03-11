import func
try:
	handle = open('qq.py',mode='r',encoding='UTF-8')
	print(handle)
	#for x in handle:
	#	print(x,end='')
	print(func.doubleit(15))
except IOError:
		print('QQ Error:',e)