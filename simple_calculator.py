from tkinter import *
import customtkinter as Modern


app = Modern.CTk()  #creating cutstom tkinter window
app.geometry("300x440")
app.title('CALCULATOR')
app._set_appearance_mode("Dark")
app.resizable(width=False, height=False)



#CREATING WIDGETS
data = Modern.CTkEntry(app, width=300,corner_radius=0,font=('Century Gothic',20),fg_color="White", border_color="#152238", justify=RIGHT)

B1 = Modern.CTkButton(app, text="%",height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:DIVISION())
B2 = Modern.CTkButton(app, text="C", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:DELETE_ALL())
B3 = Modern.CTkButton(app, text="<<", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:remove())
B4 = Modern.CTkButton(app, text="÷", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="#3F51B5",font=('Century Gothic',20), command=lambda:DIVISION())
B5 = Modern.CTkButton(app, text="7", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("7"))
B6 = Modern.CTkButton(app, text="8", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("8"))
B7 = Modern.CTkButton(app, text="9", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("9"))
B8 = Modern.CTkButton(app, text="x", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="#3F51B5",font=('Century Gothic',20), command=lambda:TIMESbtn())
B9 = Modern.CTkButton(app, text="4", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("4"))
B10 = Modern.CTkButton(app, text="5", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("5"))
B11 = Modern.CTkButton(app, text="6", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("6"))
B12 = Modern.CTkButton(app, text="-", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="#3F51B5",font=('Century Gothic',20), command=lambda:MINUSbtn())
B13 = Modern.CTkButton(app, text="1", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("1"))
B14 = Modern.CTkButton(app, text="2", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("2"))
B15 = Modern.CTkButton(app, text="3", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("3"))
B16 = Modern.CTkButton(app, text="+", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="#3F51B5",font=('Century Gothic',20), command=lambda:ADDbtn())
B17 = Modern.CTkButton(app, text="+/-", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20))
B18 = Modern.CTkButton(app, text="0", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("0"))
B19 = Modern.CTkButton(app, text=".", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="Black",font=('Century Gothic',20), command=lambda:display_num("."))
B20 = Modern.CTkButton(app, text="=", height=73.3, width=75, corner_radius=0, bg_color="Black", fg_color="#3F51B5",font=('Century Gothic',20), command=lambda:EQUAL())


#POSITIONING THEM TO DISPLAY

data.grid(row=0, column=0, columnspan=4, ipady=23.7)


#FIRST ROW
B1.grid(row=1, column=0)
B2.grid(row=1, column=1)
B3.grid(row=1, column=2)
B4.grid(row=1, column=3)

#SECOND ROW
B5.grid(row=2, column=0)
B6.grid(row=2, column=1)
B7.grid(row=2, column=2)
B8.grid(row=2, column=3)

#THIRD ROW
B9.grid(row=3, column=0)
B10.grid(row=3, column=1)
B11.grid(row=3, column=2)
B12.grid(row=3, column=3)

#FOURTH ROW
B13.grid(row=4, column=0)
B14.grid(row=4, column=1)
B15.grid(row=4, column=2)
B16.grid(row=4, column=3)

#FIFTH ROW
B17.grid(row=5, column=0)
B18.grid(row=5, column=1)
B19.grid(row=5, column=2)
B20.grid(row=5, column=3)


#FUNCTIONS

def display_num(number):
    previous_num = data.get()
    data.delete(0, END)
    
    data.insert(0, previous_num+number)

def remove():
   data.delete(0, END)
def DELETE_ALL():
   data.delete(0, END)

def ADDbtn():
    add = data.get()
    data.delete(0,END)
    data.insert(0, add+"+")
def MINUSbtn():
    minus = data.get()
    data.delete(0,END)
    data.insert(0, minus+"-")
def TIMESbtn():
    mul = data.get()
    data.delete(0, END)
    data.insert(0, mul+"*")
def DIVISION():
    dev = data.get()
    data.delete(0, END)
    data.insert(0, dev+"/")
        


def EQUAL():
    whole_expression = data.get()
    # if = exist in the expression, split it where it occur, get the last index of the resulted sliced list
    # get the first element of the last sliced list even they are only one element
    if '=' in whole_expression:
        whole_expression = whole_expression.split('=')[-1:][0]
    num = str(eval(whole_expression))

    data.delete(0, END)
    data.insert(0, f"{whole_expression} = {num}")

   



app.mainloop()