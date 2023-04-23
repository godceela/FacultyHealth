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
def staffBtn():
    root.withdraw() 
    os.system('python staff.py')
    root.destroy() 

cvStaffIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvStaffIC.pack()
imgStaff = PhotoImage(file='images//staff.png')
cvStaffIC.create_image(25, 25, image=imgStaff, anchor=CENTER)
cvStaffIC.configure(background='#FBF0D7')
cvStaffIC.place(relx=0.0069, rely=0.37)

staff_label = Label(root, text="Staff", bg="#FBF0D7", fg="#497687")
staff_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
staff_label.place(relx=0.0648, rely=0.4, anchor=CENTER)
staff_label.bind("<Button-1>", lambda event: staffBtn())

# inventory icon/button
def invBtn():
    root.withdraw() 
    os.system('python inventory.py')
    root.destroy() 

cvinventoryIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvinventoryIC.pack()
imgInv = PhotoImage(file='images//inventory2.png')
cvinventoryIC.create_image(25, 25, image=imgInv, anchor=CENTER)
cvinventoryIC.configure(background='#FBF0D7') 
cvinventoryIC.place(relx=0.007, rely=0.47)

inventory_label = Label(root, text="Inventory", bg="#FBF0D7", fg="#1E3037")
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

#Medicine Record
medicinePan = Frame(root, bg="#FBF0D7")
medicinePan.place(x=210, y=39, width=500, height=350)

medListLab = Label(medicinePan, text="MEDICINE LIST", 
                font=("Microsoft JhengHei", 14, "bold"), bg="#FBF0D7", fg="#497687")
medListLab.place(relx=0.5, rely=0.07, anchor="center")

idLab = Label(medicinePan, text="Identification #", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
idLab.place(relx=0.04, rely=0.195, anchor=W)
idEntry = Entry(medicinePan, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
idEntry.place(relx=0.663, rely=0.195, anchor=CENTER)

prodNameLab = Label(medicinePan, text="Product Name", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
prodNameLab.place(relx=0.04, rely=0.31, anchor=W)
prodNameEnt = Entry(medicinePan, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
prodNameEnt.place(relx=0.663, rely=0.31, anchor=CENTER)

qtyLabel = Label(medicinePan, text="Quantity Left", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
qtyLabel.place(relx=0.04, rely=0.42, anchor=W)
qtyEntry = Entry(medicinePan, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
qtyEntry.place(relx=0.663, rely=0.42, anchor=CENTER)

#Equip Record
equipPan = Frame(root, bg="#FBF0D7")
equipPan.place(x=719, y=39, width=480, height=350)

eqLab = Label(equipPan, text="MEDICAL EQUIPMENTS AVAILABLE", 
                font=("Microsoft JhengHei", 14, "bold"), bg="#FBF0D7", fg="#497687")
eqLab.place(relx=0.5, rely=0.07, anchor="center")

idLab = Label(equipPan, text="Identification #", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
idLab.place(relx=0.04, rely=0.195, anchor=W)
idEntry = Entry(equipPan, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=28)
idEntry.place(relx=0.663, rely=0.195, anchor=CENTER)

prodNameLab = Label(equipPan, text="Equipment Name", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
prodNameLab.place(relx=0.04, rely=0.31, anchor=W)
prodNameEnt = Entry(equipPan, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=28)
prodNameEnt.place(relx=0.663, rely=0.31, anchor=CENTER)

qtyLabel = Label(equipPan, text="Quantity", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
qtyLabel.place(relx=0.04, rely=0.42, anchor=W)
qtyEntry = Entry(equipPan, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=28)
qtyEntry.place(relx=0.663, rely=0.42, anchor=CENTER)

root.mainloop()