#Simo Andreas Novikov
#Ülesanne 03
#15.03.2022

from tkinter import *

aken = Tk()
aken.title('Ülesanne 3')
aken.configure(background='black')
aken.geometry('300x150')

Label(aken, text = 'Simo Andreas Novikov \n IT-21 \n 2022', fg="red", background="black", font="Tahoma 16 bold italic").pack(side = TOP, pady = 30)

aken.resizable(0, 0)

mainloop()