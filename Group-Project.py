# 1) import
from tkinter import *
from tkinter import messagebox

# 2) workspace
ws = Tk()
ws.title("Employee Record System")
ws.geometry('550x500')

# simple lists (your pattern)
nameList = []
departmentList = []
statusList = []  # "Full-Time" or "Part-Time"

# variables for widgets
nameVar = StringVar()
deptVar = StringVar(value="Select Department")
fullTimeVar = IntVar(value=1)  # 1 = full-time, 0 = part-time

# departments for dropdown
DEPARTMENTS = ["HR", "IT", "Finance", "Sales", "Marketing", "Operations", "Legal", "Support"]

# ----- functions -----
def add_employee():
    name = nameVar.get().strip()
    dept = deptVar.get().strip()
    status = "Full-Time" if fullTimeVar.get() == 1 else "Part-Time"

    # basic error handling
    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty.")
        return
    if dept == "Select Department":
        messagebox.showerror("Input Error", "Please choose a department.")
        return

    nameList.append(name)
    departmentList.append(dept)
    statusList.append(status)

    recordsLb.insert(END, f"{name} — {dept} — {status}")
    nameVar.set("")  # clear just the name for quick adds

def del_employee(): ## We decided as a group to create a delete function and button as well.
    sel = recordsLb.curselection()
    if not sel:
        messagebox.showerror("Input Error", "Please select a record.")
        return
    idx = sel[0]
    recordsLb.delete(idx)

def edit_employee():
    sel = recordsLb.curselection()
    if not sel:
        messagebox.showerror("Edit Error", "Please select a record to edit.")
        return

    idx = sel[0]
    name = nameVar.get().strip()
    dept = deptVar.get().strip()
    status = "Full-Time" if fullTimeVar.get() == 1 else "Part-Time"

    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty.")
        return
    if dept == "Select Department":
        messagebox.showerror("Input Error", "Please choose a department.")
        return

    # update lists
    nameList[idx] = name
    departmentList[idx] = dept
    statusList[idx] = status

    # update listbox line
    recordsLb.delete(idx)
    recordsLb.insert(idx, f"{name} — {dept} — {status}")
    recordsLb.selection_set(idx)

def load_selected(event):
    sel = recordsLb.curselection()
    if not sel:
        return
    idx = sel[0]
    nameVar.set(nameList[idx])
    deptVar.set(departmentList[idx])
    fullTimeVar.set(1 if statusList[idx] == "Full-Time" else 0)

def quit_app():
    ws.destroy()

# ----- widgets -----
# Name label & entry (with border + padding)
nameLb = Label(ws, text="Name", pady=8, padx=10, bd=2, relief="raised")
nameTf = Entry(ws, textvariable=nameVar, width=32)

# Department label & dropdown (OptionMenu)
deptLb = Label(ws, text="Department", pady=8, padx=10, bd=2, relief="raised")
deptTf = OptionMenu(ws, deptVar, *DEPARTMENTS)  ##we did not use this unpacking operator in class,
                                                    ##but I could not think of another way to display Department list.(-Cameron)
# Employment Status label & checkbutton
empLb = Label(ws, text="Employment Status", pady=8, padx=10, bd=2, relief="raised")
empChk = Checkbutton(ws, text="Full-Time (uncheck for Part-Time)", variable=fullTimeVar)

# Buttons
addEmplButton = Button(ws, text="Add Employee", command=add_employee)
editEmplButton = Button(ws, text="Edit Employee", command=edit_employee)
quitButton = Button(ws, text="Quit", command=quit_app)
delEmplButton = Button(ws, text="Delete Employee", command=del_employee)


# Listbox + Scrollbar
recordsLb = Listbox(ws, width=48, height=10)
scrollbar = Scrollbar(ws, orient =VERTICAL, command=recordsLb.yview)
recordsLb.config(yscrollcommand=scrollbar.set)
recordsLb.bind("<<ListboxSelect>>", load_selected)

# ----- layout (top to bottom) -----
# 1) Name
nameLb.grid(row=0, column=0, sticky="w", padx=10, pady=8)
nameTf.grid(row=0, column=1, sticky="w", padx=10, pady=8)

# 2) Department dropdown
deptLb.grid(row=1, column=0, sticky="w", padx=10, pady=8)
deptTf.grid(row=1, column=1, sticky="w", padx=10, pady=8)

# 3) Employment status checkbutton
empLb.grid(row=2, column=0, sticky="w", padx=10, pady=8)
empChk.grid(row=2, column=1, sticky="w", padx=10, pady=8)

# 4) Add/Edit buttons
addEmplButton.grid(row=3, column=0, padx=10, pady=8, sticky="w")
editEmplButton.grid(row=3, column=1, padx=10, pady=8, sticky="w")
delEmplButton.grid(row=3, column=2, padx=10, pady=8, sticky="w") ## We decided as a group to create a delete button and function as well.


# 5) Listbox + Scrollbar (side by side)
recordsLb.grid(row=4, column=0, columnspan=2, padx=(10,0), pady=8, sticky="nsew")
scrollbar.grid(row=4, column=2, padx=(0,10), pady=8, sticky="ns")
# make the listbox area stretch a bit
ws.grid_rowconfigure(4, weight=1)
ws.grid_columnconfigure(0, weight=1)

# 6) Quit button
quitButton.grid(row=5, column=0, padx=10, pady=10, sticky="w")

# loop
ws.mainloop()
