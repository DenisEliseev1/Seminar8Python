from tkinter import *
from enter_data import *
from find_work import *

def disact ():
    win_file['state'] = 'disabled'
    btn_create['state'] = 'disabled'
    btn_export['state'] = 'disabled'
    btn_find['state'] = 'disabled'

def windowname ():
    txt_name = Label (w, text='Введите ФИО')
    txt_name.grid(column=0, row=5)
    win_name.grid (column=1, row=5)
    txt_number_name1 = Label (w,text='Введите дату рождения')
    txt_number_name1.grid(column=0, row=6)
    win_num1.grid(column=1, row=6)
    txt_number_name2 = Label (w,text='Введите должность')
    txt_number_name2.grid(column=0, row=7)
    win_num2.grid(column=1, row=7)
    txt_number_name3 = Label (w,text='Введите заработную плату')
    txt_number_name3.grid(column=0, row=8)
    win_num3.grid(column=1, row=8)

def click_menu ():
    globals()
    w.geometry ('430x250')
    disact ()
    windowname ()
    btn_number_name.grid(column=0, row=9)

def click_main ():
    globals()

    
def name_f ():
    globals()
    name_file (win_file.get())
    click_menu()

def record ():
    globals()
    record_data (str(win_file.get()), str (win_name.get()), str (win_num1.get()), str (win_num2.get()),
                 str (win_num3.get()))
def f_n_file ():
    globals ()
    click_menu()
    btn_file = Button (w, text='Поиск', command=f_name)
    btn_file.grid(column=0, row=9)


def f_name ():
    globals ()
    find_name (str(win_file.get()), str (win_name.get()), str (win_num1.get()), str (win_num2.get()),
                 str (win_num3.get()))
w = Tk()
w.title ('Список сотрудников')
w.geometry ('430x230')
txt_file = Label (w, text='Введите название справочника')
win_file = Entry (w, width=20)
txt_file.grid(column=0, row=0)
win_file.grid (column=1, row=0)
win_name = Entry (w, width=20)
win_num1 = Entry (w, width=20)
win_num2 = Entry (w, width=20)
win_num3 = Entry (w, width=20)
txt_file = Label (w, text='Введите название справочника')
btn_create = Button (w, text='Создать новый список', command=name_f)
btn_create.grid(column=0, row=1) 
btn_export = Button (w, text='Добавить в сущ. список',command=click_menu)
btn_export.grid(column=0, row=2)
btn_find = Button (w, text= 'Поиск в списке работников', command=f_n_file)
btn_find.grid(column=0, row=3)
btn_number_name = Button (w, text='Передать в список', command=record)
w.mainloop()