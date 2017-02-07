from tkinter import *
from core import *

btnfont = ('times', 20)
txtfont1 = ('times', 14)
txtfont2 = ('times', 12)

root = Tk()
root.minsize(800, 600)
root.geometry("1240x786")

# Buttonframe
frame1 = Frame(root)
frame1.pack(side=TOP)

# Textframe
frame2 = Frame(root)
frame2.pack(side=TOP)

var = IntVar()


def info_pressed():
    global chckstr
    chckstr = "info"
    todaystr, exdatestr, remdays = remaining_time(0)
    todolst, donelst = get_data("info")
    lecad = len(todolst) / remdays
    text_boxlec.config(text="Heute: %s \nKlausur: %s \nVerbleibende Tage: %d \nVL pro Tag: %f"
                         % (todaystr, exdatestr, remdays, lecad))
    todostr = ""
    donestr = ""
    n = 0
    for i in todolst:
        todostr += str(n) + " " + i + "\n"
        n += 1
    n = 0
    for i in donelst:
        donestr += str(n) + " " + i + "\n"
        n += 1
    text_boxtodo.config(text=todostr)
    text_boxdone.config(text=donestr)
    root.update()


def ti_pressed():
    global chckstr
    chckstr = "ti"
    todaystr, exdatestr, remdays = remaining_time(1)
    todolst, donelst = get_data("ti")
    lecad = len(todolst) / remdays
    text_boxlec.config(text="Heute: %s \nKlausur: %s \nVerbleibende Tage: %d \nVL pro Tag: %f"
                         % (todaystr, exdatestr, remdays, lecad))
    todostr = ""
    donestr = ""
    n = 0
    for i in todolst:
        todostr += str(n) + " " + i + "\n"
        n += 1
    n = 0
    for i in donelst:
        donestr += str(n) + " " + i + "\n"
        n += 1
    text_boxtodo.config(text=todostr)
    text_boxdone.config(text=donestr)
    root.update()


def math_pressed():
    global chckstr
    chckstr = "mathe"
    todaystr, exdatestr, remdays = remaining_time(2)
    todolst, donelst = get_data("mathe")
    lecad = len(todolst) / remdays
    text_boxlec.config(text="Heute: %s \nKlausur: %s \nVerbleibende Tage: %d \nVL pro Tag: %f"
                         % (todaystr, exdatestr, remdays, lecad))
    todostr = ""
    donestr = ""
    n = 0
    for i in todolst:
        todostr += str(n) + " " + i + "\n"
        n += 1
    n = 0
    for i in donelst:
        donestr += str(n) + " " + i + "\n"
        n += 1
    text_boxtodo.config(text=todostr)
    text_boxdone.config(text=donestr)
    root.update()


def sys_pressed():
    global chckstr
    chckstr = "sys"
    todaystr, exdatestr, remdays = remaining_time(3)
    todolst, donelst = get_data("sys")
    lecad = len(todolst) / remdays
    text_boxlec.config(text="Heute: %s \nKlausur: %s \nVerbleibende Tage: %d \nVL pro Tag: %f"
                         % (todaystr, exdatestr, remdays, lecad))
    todostr = ""
    donestr = ""
    n = 0
    for i in todolst:
        todostr += str(n) + " " + i + "\n"
        n += 1
    n = 0
    for i in donelst:
        donestr += str(n) + " " + i + "\n"
        n += 1
    text_boxtodo.config(text=todostr)
    text_boxdone.config(text=donestr)
    root.update()


def chck_pressed():
    num = int(entry.get())
    global chckstr
    if var.get() == 0:
        change_data(chckstr, num)
    elif var.get() == 1:
        change_data(chckstr, num, undo=True)
    else:
        print("ERROR:Tkinter es muy loco")
    if chckstr == "info":
        info_pressed()
    elif chckstr == "ti":
        ti_pressed()
    elif chckstr == "mathe":
        math_pressed()
    elif chckstr == "sys":
        sys_pressed()
    else:
        print("ERROR: Invalid module")



# ------Buttons------- #

info_button = Button(frame1, text="Info", command=info_pressed, font=btnfont)
info_button.grid(row=0, column=0)

ti_button = Button(frame1, text="TI", command=ti_pressed, font=btnfont)
ti_button.grid(row=0, column=1)

math_button = Button(frame1, text="Mathe", command=math_pressed, font=btnfont)
math_button.grid(row=0, column=2)

sys_button = Button(frame1, text="Systeme", command=sys_pressed, font=btnfont)
sys_button.grid(row=0, column=3)

entry = Entry(frame1, width=3, font=btnfont)
entry.grid(row=0, column=4)

chck_button = Button(frame1, text="Check!", command=chck_pressed, font=btnfont)
chck_button.grid(row=0, column=5)

q_button = Button(frame1, text="Exit", command=root.destroy, font=btnfont)
q_button.grid(row=0, column=6)

c_button = Checkbutton(frame1, text="undo", variable=var)
c_button.grid(row=1, column=5)


# ------Text------ #


text_boxlec = Message(frame2, text="Hallo!", font=txtfont1)
text_boxlec.grid(row=0, column=0)

text_boxtodo = Message(frame2, text="", font=txtfont2)
text_boxtodo.grid(row=0, column=1)

text_boxdone = Message(frame2, text="", font=txtfont2)
text_boxdone.grid(row=0, column=2)


root.mainloop()
