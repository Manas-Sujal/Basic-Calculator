# Hey Guys Welcome Back To Canvas Creations

# In This Video We Will be coding A Very simple Calculator

# Pls Like and Subscribe

from tkinter import *


# Division
def divide():
    global divide1
    global divide2
    global product
    divide1 = int(divide_first.get())
    divide2 = int(divide_second.get())
    quotient = int(divide1 / divide2)
    Label(screen5, text="").pack()
    answer = Label(screen5, text=f"The Quotient Of {divide1} / {divide2} = {quotient}", width = 300, height=2, font = ('Comic Sams MT', 13)).pack()

def division_screen():
    global screen5
    global divide_first
    global divide_second
    screen5 = Toplevel(screen1)
    screen5.geometry("350x350")
    screen5.title("Division")
    Label(screen5, text="Division", bg="gray", width=300, height=2, font=('Comics Sans MT',13)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="What Is Your First Number",width=300, height=2, font=('Comics Sans MT', 13)).pack()
    divide_first = Entry(screen5)
    divide_first.pack()
    Label(screen5, text="").pack()
    Label(screen5, text="What Is Your Second Number", width=300, height=2, font=('Comics Sans MT', 13)).pack()
    divide_second = Entry(screen5)
    divide_second.pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Quotient",command=divide, width=15, height=2, font=('Comics Sans MT', 13)).pack()




# Multiplication
def product():
    global multiply1
    global multiply2
    global product
    multiply1 = int(multiply_first.get())
    multiply2 = int(multiply_second.get())
    product = int(multiply1 * multiply2)
    Label(screen4, text="").pack()
    answer = Label(screen4, text=f"The Product Of {multiply1} * {multiply2} = {product}", width = 300, height=2, font = ('Comic Sams MT', 13)).pack()

def multiplication_screen():
    global screen4
    global multiply_first
    global multiply_second
    screen4 = Toplevel(screen1)
    screen4.geometry("350x350")
    screen4.title("Multiplication")
    Label(screen4, text="Multiplication", bg="gray", width=300, height=2, font=('Comics Sans MT',13)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text="What Is Your First Number",width=300, height=2, font=('Comics Sans MT', 13)).pack()
    multiply_first = Entry(screen4)
    multiply_first.pack()
    Label(screen4, text="").pack()
    Label(screen4, text="What Is Your Second Number", width=300, height=2, font=('Comics Sans MT', 13)).pack()
    multiply_second = Entry(screen4)
    multiply_second.pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Product",command=product, width=15, height=2, font=('Comics Sans MT', 13)).pack()




# Subtraction
def difference():
    global subtract1
    global subtract2
    global difference
    subtract1 = int(subtract_first.get())
    subtract2 = int(subtract_second.get())
    difference = int(subtract1 - subtract2)
    Label(screen3, text="").pack()
    answer = Label(screen3, text=f"The Difference Of {subtract1} - {subtract2} = {difference}", width=300, height=2,
                   font=('Comic Sams MT', 13)).pack()


def subtraction_screen():
    global screen3
    global subtract_first
    global subtract_second
    screen3 = Toplevel(screen1)
    screen3.geometry("350x350")
    screen3.title("Subtraction")
    Label(screen3, text="Subtraction", bg="gray", width=300, height=2, font=('Comics Sans MT', 13)).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="What Is Your First Number", width=300, height=2, font=('Comics Sans MT', 13)).pack()
    subtract_first = Entry(screen3)
    subtract_first.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="What Is Your Second Number", width=300, height=2, font=('Comics Sans MT', 13)).pack()
    subtract_second = Entry(screen3)
    subtract_second.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Difference", command=difference, width=15, height=2, font=('Comics Sans MT', 13)).pack()


# Addition
def sum():
    global add1
    global add2
    global sum
    add1 = int(add_first.get())
    add2 = int(add_second.get())
    sum = int(add1 + add2)
    Label(screen2, text="").pack()
    answer = Label(screen2, text=f"The Sum Of {add1} + {add2} = {sum}", width = 300, height=2, font = ('Comic Sams MT', 13)).pack()

def addition_screen():
    global screen2
    global add_first
    global add_second
    screen2 = Toplevel(screen1)
    screen2.geometry("350x350")
    screen2.title("Addition")
    Label(screen2, text="Addition", bg="gray", width=300, height=2, font=('Comics Sans MT',13)).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="What Is Your First Number",width=300, height=2, font=('Comics Sans MT', 13)).pack()
    add_first = Entry(screen2)
    add_first.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="What Is Your Second Number", width=300, height=2, font=('Comics Sans MT', 13)).pack()
    add_second = Entry(screen2)
    add_second.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Sum",command=sum, width=15, height=2, font=('Comics Sans MT', 13)).pack()



# Main Screen

def main_screen():
    global screen1
    screen1 = Tk()
    screen1.geometry("500x500")
    screen1.title("Basic Calculator")
    #Labels
    Label(screen1, text="Welcome To The Most Basic Calculator", bg="gray", width=300, height=2, font=('Comics Sans MT',13)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="What Would You Like To Do : ", width=300, height=2, font=('Comics Sans MT',13)).pack()
    Label(screen1, text="").pack()
    #Buttons
    Button(screen1, text="Addition", command = addition_screen, width=15, height=2, font=('Comic Sans MT', 13)).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Subtraction",command = subtraction_screen, width=15, height=2, font=('Comic Sans MT', 13)).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Multiplication",command=multiplication_screen, width=15, height=2, font=('Comic Sans MT', 13)).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Division",command=division_screen, width=15, height=2, font=('Comic Sans MT', 13)).pack()
    screen1.mainloop()

main_screen()