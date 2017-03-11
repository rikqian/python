import os
ls = os.linesep
class fileop(object):
	'File operation class'
	def test(self):
		print("Test the class-method")


	def filew(self):
		while True:
			fname = input("Input the file name...")
			if os.path.exists(fname):
				print("Error:%s already exists" % fname)
			else:
				break
		all = []
		print("\nEnter lines ('.' by itself to quit).\n")

		while True:
			entry = input(">>>")
			if entry == '.':
				break
			else:
				all.append(entry)

		fobj = open(fname,'w')
		fobj.writelines('%s%s' % (x,ls) for x in all)
		fobj.close
		print("Create file Done")

	def fileo(self):
		fn = input("Input file name")
		try:
			fobj = open(fn,'r')
		except(IOError,e):
			print("*** file open error:", e)
		else:
			for eachline in fobj:
				print(eachline,end='')
			fobj.close







