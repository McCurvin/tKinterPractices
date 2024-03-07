import tkinter as love
from tkinter import ttk
from tkinter.messagebox import showinfo

GUI = love.Tk()
GUI.geometry("300x200")
GUI.title("Arithmetic Operators")
#Set Window to center
SCREEN_WIDTH = GUI.winfo_screenwidth()
SCREEN_HEIGHT = GUI.winfo_screenheight()
x = (SCREEN_WIDTH - GUI.winfo_reqwidth()) / 2
y = (SCREEN_HEIGHT - GUI.winfo_reqheight()) / 2
GUI.geometry(f"+{int(x)}+{int(y)}")

def arithmetic():
    num1 = int(txtNum1. get())
    num2 = int(txtNum2.get())
    sum = num1 + num2

    msg = f"The sum of {num1} and {num2} is {sum}"
    showinfo(title="Information", message=msg)

#fx to close applic
def close():
    GUI.destroy()

#Create frames
#Frame 1
frame1 = ttk.Frame(GUI)
frame1.pack(pady=10)

#Frame2
frame2 = ttk.Frame(GUI)
frame2.pack(pady=10)

#Frame 3
frame3 = ttk.Frame(GUI)
frame3.pack(pady=10)

#num1
lblNum1 = ttk.Label(frame1, text='Enter Num1: ')
lblNum1.pack(side=love.LEFT)
txtNum1 = ttk.Entry(frame1)
txtNum1.pack()
txtNum1.focus()

#num2
lblNum2 = ttk.Label(frame2, text="Enter Num2:")
lblNum2.pack(side=love.LEFT)
txtNum2 = ttk.Entry(frame2)
txtNum2.pack(side=love.LEFT)

#addBtn
btnAdd = ttk.Button(frame3, text="Add", command=arithmetic)
btnAdd.pack(side=love.LEFT)

#closeBtn
btnClose = ttk.Button(frame3, text="Close", command=close)
btnClose.pack(side=love.LEFT)


GUI.mainloop()
