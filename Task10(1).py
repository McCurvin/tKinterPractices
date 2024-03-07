import tkinter as love
from tkinter import ttk
from tkinter.messagebox import showinfo

GUI = love.Tk()
GUI.geometry("400x200")
GUI.title("Arithmetic Operators")
#Set Window to center
SCREEN_WIDTH = GUI.winfo_screenwidth()
SCREEN_HEIGHT = GUI.winfo_screenheight()
x = (SCREEN_WIDTH - GUI.winfo_reqwidth()) / 2
y = (SCREEN_HEIGHT - GUI.winfo_reqheight()) / 2
GUI.geometry(f"+{int(x)}+{int(y)}")

def arithmetic(operation):
    num1 = int(txtNum1.get())
    num2 = int(txtNum2.get())
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiplication":
        result = num1 * num2
    elif operation == "division":
        result = num1 / num2

    msg = f"{operation} result: {result}"
    showinfo(title="Information", message=msg)

#fx to close applic
def close():
    GUI.destroy()

result = love.StringVar()

#num1
lblNum1 = ttk.Label(GUI, text='Enter Num1: ')
lblNum1.grid(row=0, column=0, padx=10, pady=5, sticky=love.W)

txtNum1 = ttk.Entry(GUI)
txtNum1.grid(row=0, column=1, padx=10, pady=10)
txtNum1.focus()

#num2
lblNum2 = ttk.Label(GUI, text="Enter Num2:")
lblNum2.grid(row=1, column=0, padx=10, pady=5, sticky=love.W)

txtNum2 = ttk.Entry(GUI)
txtNum2.grid(row=1, column=1, padx=10, pady=10)

#Spaces b etween columns
button_width = SCREEN_WIDTH / 4

#addBtn
btnAdd = ttk.Button(GUI, text="Add", command=lambda: arithmetic("add"))
btnAdd.grid(row=2, column=0, padx=5, pady=10, stick=love.W)

#subtractBtn
btnSub = ttk.Button(GUI, text="Subtract", command=lambda: arithmetic("subtract"))
btnSub.grid(row=2, column=1, padx=5, pady=10, sticky=love.W)

#multiplicationBtn
btnMul = ttk.Button(GUI, text="Multiply", command=lambda: arithmetic("multiplication"))
btnMul.grid(row=2, column=2, pady=5, sticky=love.E)

#divisionBtn
btnDiv = ttk.Button(GUI, text="Divide", command=lambda: arithmetic("division"))
btnDiv.grid(row=2, column=3, padx=5, pady=10, sticky=love.E)


#closeBtn
btnClose = ttk.Button(GUI, text="Close", command=close)
btnClose.grid(row=4,column=0,columnspan=2,stick=love.E)


GUI.mainloop()
