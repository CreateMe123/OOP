from tkinter import *
from tkinter import ttk

pay_data = {
    "Manager":              {"A": 25000, "B": 28000, "Tax%": 0.20},
    "System Administrator": {"A": 20000, "B": 23000, "Tax%": 0.15},
    "System Analyst":       {"A": 15000, "B": 17000, "Tax%": 0.12},
    "Programmer":           {"A": 10000, "B": 12000, "Tax%": 0.10},
    "Technician":           {"A":  8000, "B":  9000, "Tax%": 0.07},
    "Encoder":              {"A":  6000, "B":  6600, "Tax%": 0.05},
    "Messenger":            {"A":  5000, "B":  5500, "Tax%": 0.04},
}

def compute():
    try:
        pay_grade = pay_grade_var.get()
        position = position_combo.get()
        ot_hours = float(ot_entry.get())

        basic = pay_data[position][pay_grade]
        ot_amount = ot_hours * 0.01 * basic
        tax = pay_data[position]["Tax%"] * (basic + ot_amount)
        deduct = tax + 200
        net_pay = basic + ot_amount - deduct

        net_salary_entry.delete(0, "end")
        net_salary_entry.insert(0, f"{net_pay:.2f}")

        gross_salary_entry.delete(0, "end")
        gross_salary_entry.insert(0, f"{basic:.2f}")

        tax_entry.delete(0, "end")
        tax_entry.insert(0, f"{tax:.2f}")

        return basic, ot_amount, tax, deduct, net_pay
    except (ValueError,KeyError):
        net_salary_entry.delete(0, "end")
        net_salary_entry.insert(0, f"Not Possible")

        gross_salary_entry.delete(0, "end")
        gross_salary_entry.insert(0, f"Not Possible")

        tax_entry.delete(0, "end")
        tax_entry.insert(0, f"Not Possible")


def clear():
    net_salary_entry.delete(0, "end")
    gross_salary_entry.delete(0, "end")
    tax_entry.delete(0, "end")
    name_entry.delete(0, "end")
    ot_entry.delete(0, "end")

def show_print_view():
    try:
        print_frame = Frame(window, height=400, width=700)
        print_frame.place(x=0, y=0)

        basic, ot_amount, tax, deduct, net_pay = compute()

        Label(print_frame, text=f"Employee Name: {name_entry.get()}",        font=("Arial", 10, "bold")).place(relx=0.5, y=20,  anchor="center")
        Label(print_frame, text=f"Position: {position_combo.get()}",         font=("Arial", 10, "bold")).place(relx=0.5, y=45,  anchor="center")
        Label(print_frame, text=f"Pay Grade Type: {pay_grade_var.get()}",    font=("Arial", 10, "bold")).place(relx=0.5, y=70,  anchor="center")
        Label(print_frame, text=f"OT Hours: {ot_entry.get()}",               font=("Arial", 10, "bold")).place(relx=0.5, y=95,  anchor="center")
        Label(print_frame, text=f"OT Amount: {ot_amount:.2f}",               font=("Arial", 10, "bold")).place(relx=0.5, y=120, anchor="center")
        Label(print_frame, text=f"Basic Salary: {basic:.2f}",                font=("Arial", 10, "bold")).place(relx=0.5, y=145, anchor="center")
        Label(print_frame, text=f"SSS Contribution: {sss_entry.get()}",      font=("Arial", 10, "bold")).place(relx=0.5, y=170, anchor="center")
        Label(print_frame, text=f"Withholding Tax: {tax:.2f}",               font=("Arial", 10, "bold")).place(relx=0.5, y=195, anchor="center")
        Label(print_frame, text=f"Total Deduction: {deduct:.2f}",            font=("Arial", 10, "bold")).place(relx=0.5, y=220, anchor="center")
        Label(print_frame, text=f"Net Outcome: {net_pay:.2f}",               font=("Arial", 10, "bold")).place(relx=0.5, y=245, anchor="center")

        Button(print_frame, text="Back", command=lambda: print_frame.destroy()).place(relx=0.5, y=285, anchor="center")
    except TypeError:
        Label(print_frame, text=f"NOT POSSIBLE",               font=("Arial", 40, "bold")).place(relx=0.5, y=245, anchor="center")
        Button(print_frame, text="Back", command=lambda: print_frame.destroy()).place(relx=0.5, y=285, anchor="center")

# ── Window setup ────────────────────────────────────────────────────────────
window = Tk()
window.title("OOP ITEM 3")
window.geometry("700x400")

bg_frame = Frame(window, bg="#93c8fa", height=400, width=700)
bg_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(window, text="Payslip", font=("Arial", 15, "bold"), bg="#93c8fa").place(x=300, y=20)
bg_frame.lower()

# ── Left column inputs ───────────────────────────────────────────────────────
Label(window, text="Name:",     font=("Arial", 10), bg="#93c8fa").place(x=135, y=70)
name_entry = Entry(window, font=("Arial"), width=15)
name_entry.place(x=200, y=70)

Label(window, text="Position:", font=("Arial", 10), bg="#93c8fa").place(x=135, y=100)
positions = ["Manager", "System Administrator", "System Analyst",
             "Programmer", "Technician", "Encoder", "Messenger"]
position_combo = ttk.Combobox(window, values=positions, state="readonly")
position_combo.current(0)
position_combo.place(x=200, y=100)

Label(window, text="OT Hours:", font=("Arial", 10), bg="#93c8fa").place(x=135, y=130)
ot_entry = Entry(window, font=("Arial"), width=15)
ot_entry.place(x=200, y=130)

# ── Pay grade radio buttons ──────────────────────────────────────────────────
pay_grade_frame = Frame(window, bg="#93c8fa", bd=1, relief="solid", width=220, height=100)
pay_grade_frame.place(x=135, y=180)

Label(window, text="Pay Grade", font=("Arial", 10), bg="#93c8fa").place(x=145, y=167)

pay_grade_var = StringVar()
Radiobutton(window, text="A", value="A", bg="#93c8fa", variable=pay_grade_var).place(x=200, y=200)
Radiobutton(window, text="B", value="B", bg="#93c8fa", variable=pay_grade_var).place(x=270, y=200)

# ── Right column outputs ─────────────────────────────────────────────────────
Label(window, text="Gross Salary:", bg="#93c8fa", font=("Arial", 10)).place(x=400, y=100)
gross_salary_entry = Entry(window, width=12, font=("Arial", 10))
gross_salary_entry.place(x=490, y=100)

Label(window, text="Less", font=("Arial", 10), bg="#93c8fa").place(x=400, y=120)

Label(window, text="Tax:",  font=("Arial", 10), bg="#93c8fa").place(x=455, y=150)
tax_entry = Entry(window, width=12, font=("Arial", 10))
tax_entry.place(x=490, y=150)

Label(window, text="SSS:",  font=("Arial", 10), bg="#93c8fa").place(x=450, y=175)
sss_entry = Entry(window, width=12, font=("Arial", 10))
sss_entry.place(x=490, y=175)
sss_entry.insert(0, "200")

Label(window, text="Net Salary:", font=("Arial", 10), bg="#93c8fa").place(x=415, y=202)
net_salary_entry = Entry(window, width=12, font=("Arial", 10))
net_salary_entry.place(x=490, y=202)

# ── Action buttons ───────────────────────────────────────────────────────────
Button(window, text="Compute", command=compute).place(x=250, y=300)
Button(window, text="Clear",   command=clear).place(x=320, y=300)
Button(window, text="Print",   command=show_print_view).place(x=370, y=300)

window.mainloop()
