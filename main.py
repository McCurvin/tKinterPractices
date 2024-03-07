import tkinter as love
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

#GUI window
GUI = love.Tk()
GUI.geometry("300x200")
GUI.title("This is an Image Button Sample")
    # Basta kani mag set sa screen sa middle
#setting center
screenWidth = GUI.winfo_screenwidth()
screenHeight = GUI.winfo_screenheight()

#calculate x & y sa gitna ng screen
x = (screenWidth - GUI.winfo_reqwidth()) / 2
y = (screenHeight - GUI.winfo_reqheight()) / 2

GUI.geometry(f"+{int(x)}+{int(y)}") # ------ END SA SET SCREEN SA MIDDLE

def image_button():
    showinfo(title="Information", message="Meow!")

catImage = Image.open("IMAGES/cat.gif")
photo = ImageTk.PhotoImage(catImage)
imageButton = ttk.Button(GUI, image = photo, command = image_button)
imageButton.pack(ipadx = 5, ipady = 5, expand = True)



GUI.mainloop()


