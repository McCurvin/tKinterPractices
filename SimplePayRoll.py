import tkinter as love
from tkinter import ttk as XD
from tkinter.messagebox import showinfo
from tkinter import font

GUI = love.Tk()
GUI.geometry("350x400")
GUI.title("Payroll Calculator")
FONT_STYLE = ("Times New Roman", 10)
GUI.option_add("*Font", FONT_STYLE)

#employee deets fx
def calc_pay():
    try:
        empID = txtEmpID.get()
        name = txtName.get()
        rate = float(txtRate.get())
        hours = float(txtHours.get())
        deduct = float(txtDeduct.get())

        gross = rate * hours
        net = gross - deduct

        lblGross.config(text=f"Gross Pay: {gross:.2f}")
        lblNet.config(text=f"Net Pay: {net:.2f}")
    except ValueError:
        showinfo(title="Error", message="Enter valid values.")

#EmployeeID
lblEmpID = XD.Label(GUI, text="Employee ID\t:")
lblEmpID.grid(row=0, column=0, padx=10, pady=10, sticky="w")
txtEmpID = XD.Entry(GUI)
txtEmpID.grid(row=0, column=1, padx=10, pady=10)

# EmpName
lblName = XD.Label(GUI, text="Name\t\t:")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = XD.Entry(GUI)
txtName.grid(row=1, column=1, padx=10, pady=10)

#EmpRate
lblRate = XD.Label(GUI, text="Rate per Hour\t:")
lblRate.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtRate = XD.Entry(GUI)
txtRate.grid(row=2, column=1, padx=10, pady=10)

#EmpHours
lblHours = XD.Label(GUI, text="Hours Worked\t:")
lblHours.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtHours = XD.Entry(GUI)
txtHours.grid(row=3, column=1, padx=10, pady=10)

#Deduction
lblDeduct = XD.Label(GUI, text="Deduction\t:")
lblDeduct.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtDeduct = XD.Entry(GUI)
txtDeduct.grid(row=4, column=1, padx=10, pady=10, sticky='e')

#CalcBtn
btnCalc = XD.Button(GUI, text="Calculate", command=calc_pay)
btnCalc.grid(row=5, column=0, columnspan=3, pady=10)

#Results
lblGross = XD.Label(GUI, text="Gross Pay\t:")
lblGross.grid(row=6, column=0, padx=10, pady=10, sticky='w')

#Net
lblNet = XD.Label(GUI, text="Net Pay\t\t:")
lblNet.grid(row=7, column=0, padx=10, pady=10, sticky='w')

GUI.mainloop()
