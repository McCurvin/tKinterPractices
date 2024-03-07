from tkinter import*

GUI = Tk()
GUI.geometry("500x500")

BUTTON_WIDTH = 10
#Background setter RED
def redBG():
    GUI.configure(bg = "red")
#bg setter blue
def blueBG():
    GUI.configure(bg = 'blue')
#bg set yellow
def yellowBG():
    GUI.configure(bg = 'yellow')

#Button 1 (RED)
button1 = Button(GUI, text = "Red", fg = "white", bg = "red", width = BUTTON_WIDTH, command = redBG, relief = "groove", borderwidth = 2)
button1.pack()

#button 2 (BLUE)
button2 = Button(GUI, text = "Blue", fg = "white", bg = 'blue', width=BUTTON_WIDTH, command=blueBG, relief = "groove", borderwidth = 2)
button2.pack()

#Button 3 (YELLOW)
button3 = Button(GUI, text = "Yellow", fg = "black", bg = "Yellow", width = BUTTON_WIDTH, command = yellowBG, relief = "groove", borderwidth = 2)
button3.pack()
GUI.mainloop()