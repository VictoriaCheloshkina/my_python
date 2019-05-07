from tkinter import *
import tkinter
def rad():
    s=table_column1.get()
    if s.isdigit()==True:
        m=4/3*3.14*int(s)**3
        table_column2.config(text=m,fg='purple')
        return m
    else:
        table_column2.config(text='Ошибка')
        return 'NaN'
    
def save():
    s=rad()
    if var=='PY_VAR1':
        with open('rad.txt', 'w') as output_file:
            output_file.write(str(s))
            output_file.close()
    else:
        with open('rad.html', 'w') as output_file:
            output_file.write(str(s)+str(var))
            output_file.close()
root = Tk()

Label(text="Программа для вычисления объема сферы",fg='purple').grid(row=0, column=0,columnspan=4)
 
Label(text="Введите радиус:",fg='purple').grid(row=1, column=0,columnspan=2)
table_column1 = Entry(fg='purple')
table_column1.grid(row=1, column=2)
Label(text="Результат\nвычислений:",fg='purple').grid(row=2, column=0,columnspan=2)
table_column2 = Label()
table_column2.grid(row=2, column=2,columnspan=2)
 
Button(text="Вычислить",command=rad,fg='purple').grid(row=3, column=1,columnspan=2)
Button(text="Сохранить",command=save).grid(row=4, column=0,columnspan=2)
var = StringVar(root)
var.set("Выпадающий список")
option = OptionMenu(root, var, "Текст", "HTML")
option.grid(row=4, column=2,columnspan=2)
root.mainloop()
