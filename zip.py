all = {"jack": 2001, "beginman": 2003, "sony": 2005, "pcky": 2000}
for i in all.keys():
    print(i, all[i])

"zip exmaple"
a = [1,2,3]
b = ["a","b","c"]
for item in zip(a,b):
	print(item)
for item in zip(*zip(a,b)):
	print(item)