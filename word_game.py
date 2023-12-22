from tkinter import *
# Tkinter is the Python interface to the Tk GUI toolkit shipped with Python.
from tkinter import messagebox

import time
word_list = ["beautiful","java","library","technology"]
score = 0;
window = Tk()
# using tkinter(library for GUI) function as Tk()
window.title("Group 12-Find word")
# window title bar name
window.geometry("1000x750+0+0")


# tkinter window size
def checkspells():
    global score
    # Global variables are the one that are defined and declared outside a function
    # and we need to use them inside a function
    word = word_check.get();
    # word = word.islower()

    if word in word_list:
        # dict = Counter(word)
        flag = 1
        # for key in dict.keys():
        #     if key not in Matrix_list:
        #         flag = 0
        if flag == 1 and len(word) > 3:
            score = score + len(word)
            total = "score = " + str(score)
            label.configure(text=total)
            print(word)
        else:
            messagebox.showinfo("Check", "No matchine with above word OR word length should be greater than 3")
    else:
        print("No Word")
    # word_check.delete(0, 'end')

def refresh():
    global score
    score = 0
    checkspells()


def tick(time1=''):
    time2 = time.strftime("%M:%S")
    if time2 != time1:
        time1 = time2;
        #	timer.config(text="After 1 minute it will be closed automatically "+time2)
    #	timer.after(200,tick)


def quit_pro():
    messagebox.showinfo("Oops!!", "Time Up! Your Score", +str(score))
    # when one minute (time limit) is over
    window.destroy()
    # to close the window in tkinter


btn1 = Button(window, text="A", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="B", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="C", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="D", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="W", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=1)
btn6 = Button(window, text="X", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=1)
btn7 = Button(window, text="K", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=1)
btn8 = Button(window, text="L", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=1)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=1)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=1)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=1)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=1)

btn1 = Button(window, text="X", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=2)
btn2 = Button(window, text="E", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=2)
btn3 = Button(window, text="I", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=2)
btn4 = Button(window, text="J", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=2)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=2)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=2)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=2)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=2)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=2)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=2)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=2)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=2)

btn1 = Button(window, text="M", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=3)
btn2 = Button(window, text="A", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=3)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=3)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=3)
btn5 = Button(window, text="A", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=3)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=3)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=3)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=3)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=3)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=3)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=3)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=3)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=4)
btn2 = Button(window, text="U", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=4)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=4)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=4)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=4)
btn6 = Button(window, text="V", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=4)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=4)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=4)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=4)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=4)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=4)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=4)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=5)
btn2 = Button(window, text="T", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=5)
btn3 = Button(window, text="E", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=5)
btn4 = Button(window, text="C", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=5)
btn5 = Button(window, text="H", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=5)
btn6 = Button(window, text="N", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=5)
btn7 = Button(window, text="O", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=5)
btn8 = Button(window, text="L", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=5)
btn9 = Button(window, text="O", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=5)
btn10 = Button(window, text="G", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=5)
btn11 = Button(window, text="Y", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=5)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=5)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=6)
btn2 = Button(window, text="I", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=6)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=6)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=6)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=6)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=6)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=6)
btn8 = Button(window, text="J", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=6)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=6)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=6)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=6)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=6)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=7)
btn2 = Button(window, text="F", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=7)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=7)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=7)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=7)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=7)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=7)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=7)
btn9 = Button(window, text="A", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=7)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=7)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=7)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=7)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=8)
btn2 = Button(window, text="U", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=8)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=8)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=8)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=8)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=8)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=8)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=8)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=8)
btn10 = Button(window, text="V", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=8)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=8)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=8)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=9)
btn2 = Button(window, text="L", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=9)
btn3 = Button(window, text="I", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=9)
btn4 = Button(window, text="B", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=9)
btn5 = Button(window, text="R", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=9)
btn6 = Button(window, text="A", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=9)
btn7 = Button(window, text="R", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=9)
btn8 = Button(window, text="Y", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=9)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=9)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=9)
btn11 = Button(window, text="A", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=9)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=9)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=10)
btn2 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=10)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=10)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=10)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=10)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=10)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=10)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=10)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=10)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=10)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=10)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=10)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=11)
btn2 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=11)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=11)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=11)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=11)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=11)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=11)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=11)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=11)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=11)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=11)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=11)

btn1 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn1.grid(column=1, row=12)
btn2 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn2.grid(column=2, row=12)
btn3 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn3.grid(column=3, row=12)
btn4 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn4.grid(column=4, row=12)
btn5 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn5.grid(column=5, row=12)
btn6 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn6.grid(column=6, row=12)
btn7 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn7.grid(column=7, row=12)
btn8 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn8.grid(column=8, row=12)
btn9 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn9.grid(column=9, row=12)
btn10 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn10.grid(column=10, row=12)
btn11 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn11.grid(column=11, row=12)
btn12 = Button(window, text="", bg="White", fg="Black", width=3, height=1, font=('Helvetica', '20'))
btn12.grid(column=12, row=12)

word_check = Entry(window, width=30, bd=0)
# widget entry to give input
word_check.configure(highlightbackground="red", highlightcolor="red")
word_check.place(x=750, y=200)
word_check.focus()
btncheck = Button(window, text="Submit", bg="purple", fg="white", width=5, font=('Helvetica', '10'), command=checkspells)
btnrefresh = Button(window, text="Refresh", bg="purple", fg="white", width=5, font=('Helvetica', '10'), command=refresh)
btncheck.place(x=820, y=250)
btnrefresh.place(x=820, y=350)
label = Label(window, text="Score = 0")
label.place(x=810, y=160)
timer = Label(window, text="You have 1 minute")
timer.place(x=790, y=300)
tick()
window.after(60000, quit_pro)
window.mainloop()
# [nltk_data]
# Error
# loading
