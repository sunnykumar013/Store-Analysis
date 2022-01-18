# import all module
from tkinter import *
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("D:\store management software\database\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self,master,*args,**kwargs):

        self.master=master
        self.heading = Label(master, text = "Add to database", font=("arial 40 bold"),fg='steel blue')
        self.heading.place(x = 500, y = 0)

        

        # label and entries forwindow
        self.name_l = Label(master,text ="enter product name",font=('arial 18 bold'))
        self.name_l.place(x=0,y=70)

        self.stock_l = Label(master,text ="enter item added",font=('arial 18 bold'))
        self.stock_l.place(x=0,y=120)

        self.cp_l = Label(master,text ="enter cost price",font=('arial 18 bold'))
        self.cp_l.place(x=0,y=170)

        self.sp_l = Label(master,text ="enter selling price",font=('arial 18 bold'))
        self.sp_l.place(x=0,y=220)

        self.vendor_l = Label(master,text ="enter vendor name",font=('arial 18 bold'))
        self.vendor_l.place(x=0,y=270)

        self.vendor_phone_l = Label(master,text ="enter vendor phone number ",font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0,y=320)

        self.id_l = Label(master,text ="enter ID ",font=('arial 18 bold'))
        self.id_l.place(x=0,y=370)

        # entries for lebel
        self.name_e = Entry(master,width=25,font=('arial 18 bold'))
        self.name_e.place(x=380,y=70)

        self.stock_e = Entry(master,width=25,font=('arial 18 bold'))
        self.stock_e.place(x=380,y=120)

        self.cp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.cp_e.place(x=380,y=170)

        self.sp_e = Entry(master,width=25,font=('arial 18 bold'))
        self.sp_e.place(x=380,y=220)

        self.vendor_e = Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_e.place(x=380,y=270)

        self.vendor_phone_e = Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380,y=320)

        self.id_e = Entry(master,width=25,font=('arial 18 bold'))
        self.id_e.place(x=380,y=370)

        



        # button

        self.btn_add = Button(master,text ="Add to database",width = 25,height =2,bg='steelblue',fg='white',command=self.get_items)
        self.btn_add.place(x=520,y=420)

        self.btn_clear = Button(master,text ="Clear All Field",width = 18,height =2,bg='lightgreen',fg='white',command=self.clear_all)
        self.btn_clear.place(x=350,y=420)

        # text box for logs

        self.tBox = Text(master,width=60,height=18)
        self.tBox.place(x=750,y=70)
        self.tBox.insert(END,"ID has reached upto:"+str(id))
        self.tBox.place(x=750,y=70)

        self.master.bind('<Return>',self.get_items)
        self.master.bind('<Up>',self.clear_all)

    def get_items(self,*args,**kwargs):
        # get entries
        self.name = self.name_e.get()
        self.stock= self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp=self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        # dynamic entries
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name =='' or self.stock ==''or self.cp =='' or self.sp =='':
            tkinter.messagebox.showinfo('Error','Please Fill all the entries')
        else:
            sql = "INSERT INTO inventory(name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phoneno)VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendor_phone))
            conn.commit()
            #textbox insert
            self.tBox.insert(END,"\n\nInseted"+ str(self.name) + "into the database with code " + str(self.id_e.get()) )
            tkinter.messagebox.showinfo("Success","successfully added to the database.")
        
    def clear_all(self,*args,**kwargs):
        
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phone_e.delete(0,END)
        self.id_e.delete(0,END)







root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Add to database")
root.mainloop()
