import tkinter as love
from tkinter import ttk
from tkinter.messagebox import showinfo

#GUI window
GUI = love.Tk()
GUI.geometry("300x200")
GUI.title("Arithmetic Operators")
#Set screen middle
SCREEN_WIDTH = GUI.winfo_screenwidth()
SCREEN_HEIGHT = GUI.winfo_screenheight()
x = (SCREEN_WIDTH - GUI.winfo_reqwidth()) / 2
y = (SCREEN_HEIGHT - GUI.winfo_reqheight()) / 2
GUI.geometry(f"+{int(x)}+{int(y)}")

#arithmetic
def arithmetic():
    num1 = int(txtNum1.get())
    num2 = int(txtNum2.get())
    sum = num1 + num2

    msg = f"The sum of {num1} and {num2} is {sum}"
    showinfo(title= "Information", message=msg)
#close
def close():
    GUI.destroy()

lblNum1 = ttk.Label(GUI, text = "Enter Num1: ")
lblNum1.pack()
txtNum1 = ttk.Entry(GUI)
txtNum1.pack()
txtNum1.focus()
lblNum2 = ttk.Label(GUI, text = "Enter Num2: ")
lblNum2.pack()
txtNum2 = ttk.Entry(GUI)
txtNum2.pack()
txtNum2.focus()

#Buttons
btnAdd = ttk.Button(GUI, text= 'Add', command = arithmetic)
btnAdd.pack()
btnClose = ttk.Button(GUI, text = 'Close', command = close)
btnClose.pack()


GUI.mainloop()