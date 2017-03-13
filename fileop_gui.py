import tkinter as tk
import os
#use the line seperator defined in different os
ls = os.linesep
top = tk.Tk()


#b.bind(sequence='ButtonRelease',func='save()')
#define the text box 
t = tk.Text()
#b.place(relwidth= 1,relheight= 0.5)

f = open("test.txt",'r')
n = 1.0
#for i in f:
#t.edit_modified()
for i in f:
	t.insert(n,i)
	n += 1
#print(t.index(1.0))

def save():
	print("------------Press button-------------")
#the 'end' means the end INDEX of text
	print(t.get(1.0,'end'))
	fw = open("test.txt",'w')
	for i in t.get(1.0,'end'):
		fw.writelines('%s' % (i))
		
#create button with label 'Save' and event 'save'
b = tk.Button(text='Save',command=save)
b.pack(fill = 'x', ipady = 0.5)
t.pack()	

top.mainloop()
#print("Test")