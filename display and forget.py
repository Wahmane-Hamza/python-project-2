from tkinter import *
import time

window = Tk()
window['bg'] = "#556"
window.title("HAMZA")
window.geometry("1000x550+250+150")
window.resizable(False, False)


# -----------------------------------------------------------------------------------------




def red() :

    global frm_red
    lbl_red['text'] = str(int(lbl_red['text']) + 1)
    if lbl_red['text'] == str(1) :
        frm_red = Frame(height=100, width=100, bg='#f00')
        frm_red.place(x=300, y=200)
        # forget green frame
        frm_green.place_forget()

    lbl_green['text'] = str(0)





def green() :

    global frm_green
    lbl_green['text'] = str(int(lbl_green['text']) + 1)
    if lbl_green['text'] == str(1) :
        frm_green = Frame(height=100, width=100, bg='#0f0')
        frm_green.place(x=600, y=200)
        # forget red frame
        frm_red.place_forget()

    lbl_red['text'] = str(0)


# -------------------------------------------------------------------------------------------










# ---------------------------------------------------------------------------------

lbl_red = Label(text=str(0),font=('Arial',15))


# Button to display red
btn_red = Button(text='Display red', command=red)
btn_red.place(x=320, y=350)
# --------------------------------------------------


# --------------------------------------------------

lbl_green = Label(text=str(0),font=('Arial',15))


# Button to display green
btn_green = Button(text='Display green', command=green)
btn_green.place(x=620, y=350)
# -----------------------------------------------------------------------------------


window.mainloop()
