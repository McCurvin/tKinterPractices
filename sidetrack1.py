import tkinter as love

GUI = love.Tk()
GUI.geometry("300x200")

def getText():
    value = txtType.get()
    lblDisplay.config(text=f"You entered: {value}")

#CREATE ENTRY WIDGET
txtType = love.Entry(GUI)
txtType.pack()

#Create entered text btn
btnClick = love.Button(GUI, text = "Get Text", command=getText)
btnClick.pack()

lblDisplay = love.Label()
lblDisplay.pack()

GUI.mainloop()
