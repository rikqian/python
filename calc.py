class B():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def by(self):
		return self.a*self.b

# b = B(2,3)
# print(b.by())

class rn():
	def c(self,n):
		x = int(n)%4
		y = int(n)%100
		print(x,y)
		s = False
		if (x == 0) and (y==0):
			s = True
		elif (x == 0) and (y != 0):
			s = True
		else:
			s = False
		return s
# c = rn()
# print(c.c(1960))

#列表解析找偶数
s = [i for i in range(20) if (i%2 == 0)]
for m in s:
	print(m)
