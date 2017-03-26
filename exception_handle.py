def error1():
    try:
        f = open('ttt.xt', 'r')
    except IOError as e:
        print("Could not open file:", e)


def safe_float(obj):
    try:
        r = float(obj)
    # Once an error occurs,the r can not be valued
    except (ValueError, TypeError):
        r = 'Invalid value or type'
    # Once there is an error, else statement will not be executed
    else:
        print('test')
    return print(r)


def with_ex():
	with open("test.txt",'r') as f:
		for c in [line.strip() for line in f]:
			print(c)
	print("value")

safe_float('xxss')
with_ex()
