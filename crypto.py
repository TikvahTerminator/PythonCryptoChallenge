import tkinter as tk
from tkinter import *
alphabet = [[[["a","b","c"],["d","e","f"]],[["g","h","i"],["j","k","l"]]],[[["m","n","o"],["p","q","r"]],[["s","t","u"],["v","w","x","y","z"]]]]
gui = Tk()

def readme(s):
	initial = s.split(":")
	v = []
	for i in range(0,len(initial)):
		v.append(initial[i].split(","))
	starter = "";
	for j in range(0, len(v)):
		try:
			starter = starter + alphabet[int(v[j][0])][int(v[j][1])][int(v[j][2])][int(v[j][3])]
		except ValueError:
				break
	return starter

def makeme(s):
	a = list(s.replace(" ","").lower())
	d = ""
	for i in range(0,len(a)):
		for q in range(0,len(alphabet)): ## first value for code
			for w in range(0,len(alphabet[q])):
				for e in range(0,len(alphabet[q][w])):
					for r in range(0,len(alphabet[q][w][e])):
						if a[i] is alphabet[q][w][e][r]:
							d = d + str(q)+","+str(w)+","+str(e)+","+str(r)+":"
	return d

def printresult(s,txbox):
	txbox.delete("1.0","end-1c")
	txbox.insert("end-1c",readme(s))
	return "break" 
def main():
	gui.title("Super Secret Encoder!") 
	main = Frame(gui, background="#ff0000")
	main.pack(fill=X)
	swidth = gui.winfo_screenwidth()
	sheight = gui.winfo_screenheight()
	windowsize = str((int(swidth*0.2))) + "x" + str((int(sheight*0.15))) 
	gui.geometry(windowsize)
	Label(main, text="Use this to decode our messages!", bg="#ff0000", fg="white").grid(row=0,column=0)
	subframe = Frame(main, background = "#ff0000")
	subframe.grid(row=1,column=0)
	Label(subframe, text="text to  Encrypt: ", bg="#ff0000", fg="white").grid(row=0,column=0)
	tbox = Text(subframe, height = 1, width=30)
	tbox.bind('<Return>', lambda event: printresult(tbox.get("1.0","end-1c"),txbox))
	tbox.grid(row=0,column=1, padx=(10,10))
	txbox = Text(main, height = 4, width = 50) 
	en = Button(main, text="Decrypt", command=lambda: printresult(tbox.get("1.0", "end-1c"),txbox)).grid(row=2, column=0)
	txbox.grid(row=3,column=0)
	gui.mainloop()
main()
