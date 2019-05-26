from tkinter import *
from tkinter import messagebox as mb
import json

def todolist():
    with open("qw.json", 'r') as output_file:
        e4.config(text = output_file.read())
    
def writer():    
    d1 = e1.get()
    d2 = e2.get()
    d3 = e3.get()
    try:
        with open("qw.json", 'a') as output_file:
            output_file.write('Задача:'+d1+" Категория:"+d2+" Время:"+d3+"\n")
    except Exception as e:
        print(e)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

def close_window():
    answer = mb.askyesno(title = "Выход", message = "Вы уверены, что хотите выйти?")
    if answer == True:
        window.destroy()

window = Tk()
window.resizable(False, False)
window.geometry('+450+180')
window.config(bg = 'black')
window.title('Менеджер задач')

l1 = Label(text = "Задача:",fg = 'white',bg = 'black',font =("Times", "16", "bold italic"))
l1.grid(row=0, column=0)
l2 = Label(text = "Категория:",fg = 'white',bg = 'black',font =("Times", "16", "bold italic"))
l2.grid(row=1, column=0)
l2.config(bg = 'black')
l3 = Label(text = "Время:",fg = 'white',bg = 'black',font =("Times", "16", "bold italic"))
l3.grid(row=2, column=0)
l3.config(bg = 'black')

e1 = Entry(fg = 'black',borderwidth = '3',font =("Times", "12", "bold"))
e1.grid(row=0, column=1,columnspan=2)
e2 = Entry(fg = 'black',borderwidth = '3',font =("Times", "12", "bold"))
e2.grid(row=1, column=1,columnspan=2)
e3 = Entry(fg = 'black',borderwidth = '3',font =("Times", "12", "bold"))
e3.grid(row=2, column=1,columnspan=2)
e4 = Label(fg = 'white',bg = 'black',font =("Times", "12", "bold italic"))
e4.grid(row=0, column=3,columnspan=4,rowspan=6, sticky = W + E + N + S)


b1 = Button(text = "Добавить",relief = "ridge",fg = 'black',bg = 'white', activebackground='black',activeforeground='white',font =("Times", "10", "bold"),command = writer)
b1.grid(row=3, column=1)
b2 = Button(text = "Список задач",fg = 'black',relief = "ridge",bg = 'white', activebackground='black',activeforeground='white',font =("Times", "10", "bold"), command = todolist)
b2.grid(row=4, column=1)
b3 = Button(text = "Выход",fg = 'black',relief = "ridge",bg = 'white', activebackground='black',activeforeground='white',font =("Times", "10", "bold"), command = close_window)
b3.grid(row=5, column=1)

window.mainloop()
