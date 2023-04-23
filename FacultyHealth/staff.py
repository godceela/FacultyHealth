from tkinter import *
from tkinter.ttk import *
from tkinter import *
import os

root = Tk()
root.config(highlightthickness=0, background="#DFEEED")

window_width = 1250
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.overrideredirect(True)

#Exit Form
def exitForm():
    root.withdraw() 
    root.destroy() 

exitLogo = Canvas(root, width=30, height=30, highlightthickness=0) 
exitLogo.pack()
imgExitLogo = PhotoImage(file='images//exit.png')
exitLogo.create_image(15, 15, image=imgExitLogo, anchor=CENTER)
exitLogo.configure(background='#DFEEED', cursor="hand2")
exitLogo.place(relx=0.97, rely=0.009)
exitLogo.bind("<Button-1>", lambda event: exitForm())

sidebar_frame = Frame(root, bg="#FBF0D7")
sidebar_frame.place(relx=0, rely=0, relheight=1, relwidth=0.14)

# sidebar logo
cvsbrLogo = Canvas(root, width=100, height=80, highlightthickness=0) 
cvsbrLogo.pack()
imgsbrLogo = PhotoImage(file='images//sbrLogo.png')
cvsbrLogo.create_image(48, 44, image=imgsbrLogo, anchor=CENTER)
cvsbrLogo.configure(background='#FBF0D7')
cvsbrLogo.place(relx=0.03, rely=0.043)

# home icon/button
def homeBtn():
    root.withdraw() 
    os.system('python homepage.py')
    root.destroy() 

cvHomeIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvHomeIC.pack()
imgHome = PhotoImage(file='images//home.png')
cvHomeIC.create_image(25, 25, image=imgHome, anchor=CENTER)
cvHomeIC.configure(background='#FBF0D7')
cvHomeIC.place(relx=0.0069, rely=0.17)

home_label = Label(root, text="Home", bg="#FBF0D7", fg="#497687")
home_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
home_label.place(relx=0.07, rely=0.2, anchor=CENTER)
home_label.bind("<Button-1>", lambda event: homeBtn())

# patient icon/button
def ptntBtn():
    root.withdraw() 
    os.system('python patient.py')
    root.destroy() 

cvPtntIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvPtntIC.pack()
imgPtnt = PhotoImage(file='images//patient.png')
cvPtntIC.create_image(25, 25, image=imgPtnt, anchor=CENTER)
cvPtntIC.configure(background='#FBF0D7')
cvPtntIC.place(relx=0.0069, rely=0.27)

patient_label = Label(root, text="Patient", bg="#FBF0D7", fg="#497687")
patient_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
patient_label.place(relx=0.071, rely=0.3, anchor=CENTER)
patient_label.bind("<Button-1>", lambda event: ptntBtn())


# staff icon/button
cvStaffIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvStaffIC.pack()
imgStaff = PhotoImage(file='images//staff2.png')
cvStaffIC.create_image(25, 25, image=imgStaff, anchor=CENTER)
cvStaffIC.configure(background='#FBF0D7')
cvStaffIC.place(relx=0.0069, rely=0.37)

staff_label = Label(root, text="Staff", bg="#FBF0D7", fg="#1E3037")
staff_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
staff_label.place(relx=0.0648, rely=0.4, anchor=CENTER)

# inventory icon/button
def invBtn():
    root.withdraw() 
    os.system('python inventory.py')
    root.destroy() 

cvinventoryIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvinventoryIC.pack()
imgInv = PhotoImage(file='images//inventory.png')
cvinventoryIC.create_image(25, 25, image=imgInv, anchor=CENTER)
cvinventoryIC.configure(background='#FBF0D7') 
cvinventoryIC.place(relx=0.007, rely=0.47)

inventory_label = Label(root, text="Inventory", bg="#FBF0D7", fg="#497687")
inventory_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
inventory_label.place(relx=0.078, rely=0.5, anchor=CENTER)
inventory_label.bind("<Button-1>", lambda event: invBtn())

# logout icon/button
def logoutBtn():
    root.withdraw() 
    os.system('python login_admin.py')
    root.destroy() 

cvLogoutIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvLogoutIC.pack()
imgLogout = PhotoImage(file='images//logout.png')
cvLogoutIC.create_image(25, 25, image=imgLogout, anchor=CENTER)
cvLogoutIC.configure(background='#FBF0D7') 
cvLogoutIC.place(relx=0.009, rely=0.88)

logout_label = Label(root, text="Logout", bg="#FBF0D7", fg="#497687")
logout_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
logout_label.place(relx=0.065, rely=0.91, anchor=CENTER) 
logout_label.bind("<Button-1>", lambda event: logoutBtn())

#main screen
# STAFF AND NURSE INFO
infoPanel = Frame(root, bg="#FBF0D7")
infoPanel.place(x=210, y=48, width=1000, height=250)

ptntRec = Label(infoPanel, text="STAFF'S INFORMATION", 
                font=("Microsoft JhengHei", 14, "bold"), bg="#FBF0D7", fg="#497687")
ptntRec.grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

idLabel = Label(infoPanel, text="Identification #", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687")
idLabel.grid(row=1, column=0, padx=20, pady=10, sticky="w")
idEntry = Entry(infoPanel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
idEntry.grid(row=1, column=1, padx=20, pady=10)

nameLabel = Label(infoPanel, text="Full Name", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
nameLabel.grid(row=2, column=0, padx=20, pady=10, sticky="w")
nameEntry = Entry(infoPanel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
nameEntry.grid(row=2, column=1, padx=20, pady=10)

contLabel = Label(infoPanel, text="Contact #", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
contLabel.grid(row=3, column=0, padx=20, pady=10, sticky="w")
contEntry = Entry(infoPanel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
contEntry.grid(row=3, column=1, padx=20, pady=10)

addressLabel = Label(infoPanel, text="Address", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
addressLabel.grid(row=4, column=0, padx=20, pady=10, sticky="w")
addressEntry = Entry(infoPanel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
addressEntry.grid(row=4, column=1, padx=1, pady=10)

sexLabel = Label(infoPanel, text="Sex", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
sexLabel.grid(row=1, column=2, padx=20, pady=10, sticky="w")
sexCmBox = Combobox(infoPanel, font=("Microsoft JhengHei", 11), 
                            values=["Male", "Female"], width=30)
sexCmBox.grid(row=1, column=3, padx=10, pady=10)

usnLabel = Label(infoPanel, text="Username", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
usnLabel.grid(row=2, column=2, padx=20, pady=10, sticky="w")
usnEntry = Entry(infoPanel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
usnEntry.grid(row=2, column=3, padx=20, pady=10)

noteLabel = Label(infoPanel, text="*Username and password will serve as staff's login info.", 
                 font=("Microsoft JhengHei", 8, "italic"), bg="#FBF0D7", fg="gray")
noteLabel.place(relx=0.769, rely=0.75, anchor=CENTER)

passLabel = Label(infoPanel, text="Password", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
passLabel.place(relx=0.545, rely=0.65, anchor=CENTER)
passEntry = Entry(infoPanel, show="•", font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=28)
passEntry.place(relx=0.756, rely=0.65, anchor=CENTER)

def passVisibility():
    if passEntry['show'] == '':
        passEntry.configure(show='•')
        btnShow.configure(text='Show')
    else:
        passEntry.configure(show='')
        btnShow.configure(text='Hide')

btnShow = Button(infoPanel, text='Show', command=passVisibility,
                              bg='#497687', fg='#ffffff')
btnShow.config(font=("Microsoft JhengHei", 7),cursor="hand2")
btnShow.place(relx=0.905, rely=0.65, anchor=CENTER)

def reset():
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    passEntry.delete(0, END)
    usnEntry.delete(0, END)
    addressEntry.delete(0, END)
    contEntry.delete(0, END)
    sexCmBox.set("")

btnReset = Button(root, text="Reset", command=reset, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnReset.place(relx=0.817, rely=0.4, anchor=CENTER)

def delete():
    #tempo-command
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    passEntry.delete(0, END)
    usnEntry.delete(0, END)
    addressEntry.delete(0, END)
    sexCmBox.set("")

btnNew = Button(root, text="Delete", command=delete, 
                      bg="#497687", fg="#ffffff")
btnNew.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnNew.place(relx=0.865, rely=0.4, anchor=CENTER)

def new():
    #tempo-command
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    passEntry.delete(0, END)
    usnEntry.delete(0, END)
    addressEntry.delete(0, END)
    sexCmBox.set("")

btnSave = Button(root, text="New", command=new, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSave.place(relx=0.91, rely=0.4, anchor=CENTER)

def add():
    #tempo-command
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    passEntry.delete(0, END)
    usnEntry.delete(0, END)
    addressEntry.delete(0, END)
    sexCmBox.set("")

btnSave = Button(root, text="Add", command=add, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSave.place(relx=0.95, rely=0.4, anchor=CENTER)


root.mainloop()