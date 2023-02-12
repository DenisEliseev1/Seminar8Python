import user_interface
from tkinter import *
def find_name (n,x=0,y=0,z=0,w=0):
    name = n+'.txt'
    f = open (name, 'r')
    for i in f:
        if j[0].find == str(x) or j[1].find == str(y) or j[2].find == str(z) or j[3].find == str(w):
            for j in i.split(','):            
                win = Tk()
                win.title ('Список сотрудников')
                win.geometry ('430x230') 
                txt1 = Label (win, text= f'ФИО {j[0]}')
                txt1.grid (column=0, row=0)
                txt1 = Label (win, text= f'Дата рождения {j[1]}')
                txt1.grid (column=0, row=0)
                txt1 = Label (win, text= f'Должность {j[2]}')
                txt1.grid (column=0, row=0)
                txt1 = Label (win, text= f'Зарплата {j[3]}')
                txt1.grid (column=0, row=0)
    f.close
f = open ('2.txt', 'r')

        
f.close