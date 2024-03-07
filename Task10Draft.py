import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def arithmetic():
    num1 = int(txtNum1.get())
    num2 = int(txtNum2.get())
    sum = num1 + num2
    msg = f"The	sum	of	{num1} and	{num2} is	{sum}"
    showinfo(title="Information", message=msg)


# 	Create	a	function	to	close	the	application
def close():
    gui.destroy()


# 	Create	the	main	GUI	window
gui = tk.Tk()
gui.geometry("300x200")
gui.title("Arithmetic	Operators")
gui.eval("tk::PlaceWindow	.	center")
# 	Create	StringVar	to	hold	the	result
result = tk.StringVar()
# 	Labels	and	Entry	widgets	using	the	grid	manager
lblNum1 = ttk.Label(gui, text="Enter Num1:")
lblNum1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
txtNum1 = ttk.Entry(gui)
txtNum1.grid(row=0, column=1, padx=10, pady=10)
txtNum1.focus()
lblNum2 = ttk.Label(gui, text="Enter Num2:")
lblNum2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
txtNum2 = ttk.Entry(gui)
txtNum2.grid(row=1, column=1, padx=10, pady=10)
# 	Buttons	using	the	grid	manager
btnAdd = ttk.Button(gui, text="Add", command=arithmetic)
btnAdd.grid(row=2, column=0, columnspan=2, pady=10)
btnClose = ttk.Button(gui, text="Close", command=close)
btnClose.grid(row=2, column=1, columnspan=2, sticky=tk.E)
gui.mainloop()
