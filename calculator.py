from tkinter import *
#calypso orange,fruity cocktail,soft marigold
def onclick(event):
    global numbers
    text=event.widget.cget("text")#cget fuction gives text of clicked button
    if text=="=":
        if numbers.get().isdigit():
            change_numbers=int(numbers.get())#if text(numbers) is a digit then change it to integer
        else:
            change_numbers=eval(numbers.get())#if text(numbers) is a expression then eveluate the expession
        numbers.set(change_numbers)
        scrn.update()
    elif text=="Clear":
        numbers.set("")
        scrn.update()
    else:
        numbers.set(numbers.get()+text)
        scrn.update()
win=Tk()
win.geometry("650x700")
win.title("Simple Calculator")
numbers=StringVar()
numbers.set("")
scrn=Entry(win,text=numbers,font='lucida 30 bold',bg='dim gray',fg='white')
scrn.pack(fill='both',pady=5)

f=Frame(win)
b=Button(f,text='Clear',font='lucida 36 bold',padx='10',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='%',font='lucida 36 bold',padx='8',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='/',font='lucida 36 bold',padx='14',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
f.pack()

f=Frame(win)
b=Button(f,text='7',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='8',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='9',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='*',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
f.pack()

f=Frame(win)
b=Button(f,text='4',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='5',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='6',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='-',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
f.pack()

f=Frame(win)
b=Button(f,text='1',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='2',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='3',font='lucida 36 bold',padx='12',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='+',font='lucida 36 bold',padx='7',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
f.pack()

f=Frame(win)
b=Button(f,text='0',font='lucida 36 bold',padx='28',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='.',font='lucida 36 bold',padx='32',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
b=Button(f,text='=',font='lucida 36 bold',padx='28',pady='12',bg="orange",fg='white')
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",onclick)
f.pack()


win.mainloop()