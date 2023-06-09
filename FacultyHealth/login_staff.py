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

#side image
canvas = Canvas(root, width=515, height=665, highlightthickness=0) 
canvas.pack()
image = PhotoImage(file='images//logo-loginView.png')
canvas.create_image(266, 319, image=image, anchor=CENTER)
canvas.place(relx=0.07, rely=0.07)

# admin icon
canvasAdminIc = Canvas(root, width=50, height=50, highlightthickness=0) 
canvasAdminIc.pack()
imageAdminIc = PhotoImage(file='images//admin.png')
canvasAdminIc.create_image(25, 25, image=imageAdminIc, anchor=CENTER)
canvasAdminIc.configure(background='#DFEEED') 
canvasAdminIc.place(relx=0.717, rely=0.77)


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "username" and password == "1234":
        message_label.config(text="Login successful!", fg="green")
    else:
        message_label.config(text="Login failed. Please try again.", fg="#b12a2a")

WC_label = Label(root, text="W", bg="#DFEEED", fg="#497687")
WC_label.config(font=("Matura MT Script Capitals", 30, "bold"))
WC_label.place(relx=0.638, rely=0.2, anchor=CENTER)

WC2_label = Label(root, text="elcome back, ", bg="#DFEEED", fg="#497687")
WC2_label.config(font=("Microsoft JhengHei", 30, "bold"))
WC2_label.place(relx=0.768, rely=0.2, anchor=CENTER)

staff_label = Label(root, text="Staff!", bg="#DFEEED", fg="#b12a2a")
staff_label.config(font=("Matura MT Script Capitals", 65))
staff_label.place(relx=0.73, rely=0.3, anchor=CENTER)

username_label = Label(root, text="Username", bg="#DFEEED", fg="#497687")
username_label.config(font=("Microsoft JhengHei", 13, "bold"))
username_label.place(relx=0.66, rely=0.4, anchor=CENTER)

username_entry = Entry(root, bg="#FFFFFF", fg="#497687")
username_entry.config(font=("Microsoft JhengHei", 13),cursor="hand2")
username_entry.place(relx=0.78, rely=0.4, anchor=CENTER)

password_label = Label(root, text="Password", bg="#DFEEED", fg="#497687")
password_label.config(font=("Microsoft JhengHei", 13, "bold"))
password_label.place(relx=0.658, rely=0.45, anchor=CENTER)

password_entry = Entry(root, show="•", bg="#FFFFFF", fg="#497687")
password_entry.config(font=("Microsoft JhengHei", 13),cursor="hand2")
password_entry.place(relx=0.78, rely=0.45, anchor=CENTER)

login_button = Button(root, text="Login", command=login, 
                      bg="#497687", fg="#ffffff")
login_button.config(font=("Microsoft JhengHei", 11), cursor="hand2")
login_button.place(relx=0.81, rely=0.58, anchor=CENTER)

message_label = Label(root, text="", bg="#DFEEED")
message_label.config(font=("Microsoft JhengHei ", 11))
message_label.place(relx=0.78, rely=0.63, anchor=CENTER)

def passVisibility():
    if password_entry['show'] == '':
        password_entry.configure(show='•')
        btnShow.configure(text='Show password')
    else:
        password_entry.configure(show='')
        btnShow.configure(text='Hide password')

btnShow = Button(root, text='Show password', command=passVisibility,
                              bg='#94A2A7', fg='#ffffff')
btnShow.config(font=('Microsoft JhengHei', 8),cursor="hand2")
btnShow.place(relx=0.778, rely=0.49, anchor=CENTER)

def reset():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    message_label.config(text="", fg="#000000")

btnReset = Button(root, text="Reset", command=reset, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnReset.place(relx=0.75, rely=0.58, anchor=CENTER)

def open_adminLogin():
    root.withdraw() 
    os.system('python login_admin.py')
    root.destroy() 

adminLogin_label = Label(root, text="Admin Login", bg="#DFEEED", fg="#497687")
adminLogin_label.config(font=("Microsoft JhengHei", 13, "bold"), cursor="hand2")
adminLogin_label.place(relx=0.8, rely=0.8, anchor=CENTER)
adminLogin_label.bind("<Button-1>", lambda event: open_adminLogin())

root.mainloop()
