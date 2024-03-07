import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

# Create three labels
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Label 3")
label3.grid(row=1, column=0, columnspan=2)  # Label 3 spans two columns

root.mainloop()
