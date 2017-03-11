class tc(object):
	def __init__(self,x='00'):
		self.x=x
		print(x)
	def sd(self):

		print("test class self",self.x)
	def sd2(self,x):
		self.x=x
		print("Again",x)
	def sd3(self):
		print("Thrid",self.x)

p=tc('AA')
p.sd()
p.sd2('aa')
p.sd3()
p1=tc()