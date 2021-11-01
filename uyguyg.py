from tkinter import*

root = Tk()
root.title("uiheiu")
root.geometry("500x600")

lname = Label(root, text = "Name: ")
lname.place(relx=0.3,rely=0.12,anchor=CENTER)

lpass = Label(root, text = "Password:")
lpass.place(relx=0.28,rely=0.19,anchor=CENTER)

lcap = Label(root, text = "Captcha: ")
lcap.place(relx=0.29,rely=0.25,anchor=CENTER)

iname = Entry(root)
iname.place(relx=0.55,rely=0.12,anchor=CENTER)

ipass = Entry(root)
ipass.place(relx=0.55,rely=0.19,anchor=CENTER)

icap = Entry(root)
icap.place(relx=0.55,rely=0.25,anchor=CENTER)

ndisp = Label(root)
ndisp.place(relx=0.4, rely=0.45)

pdisp = Label(root)
pdisp.place(relx=0.4, rely=0.55)

cdisp = Label(root)
cdisp.place(relx=0.4, rely=0.65)

class usrdb():
    def __init__(self):
        self._usrn = "Jimmy"
        self._pasw = "J1mmyD@wg81"
        self.cap = "980igy"
        
    def showusr(self):
        ndisp['text'] = "Name: " + self._usrn
        pdisp['text'] ="Password: " + self._pasw
        cdisp['text'] ="Captcha: " + self.cap
        
usr = usrdb()

def addusr():
    global usr
    usr.usrn = str(iname.get())
    usr.pasw = str(ipass.get())
    usr.cap = str(icap.get())
    print("details updated")

btnadd = Button(root, text="Add User", command=addusr)
btnadd.place(relx=0.3, rely=0.35, anchor=CENTER)

btnshow = Button(root, text="Show detalis", command=usr.showusr)
btnshow.place(relx=0.68, rely=0.35, anchor = CENTER)

root.mainloop()