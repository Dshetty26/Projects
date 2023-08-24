from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Report_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1240x510+300+280")


        # -------------------------------------------LOGO------------------------------------------------------------------
        img_logo = Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\grandBay.jpg")
        img_logo = img_logo.resize((200, 150))
        self.photologo = ImageTk.PhotoImage(img_logo)
        lblimg = Label(self.root, image=self.photologo, border=1, relief=RIDGE)
        lblimg.place(x=15, y=0, width=200, height=150)


        # -----------------------------------------------------labelframe search system ----------------------------------------------------

        labelframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="REVIEWS",font=("arial", 15, "bold"))
        labelframeright.place(x=20, y=155, width=1200, height=450)

        # ------------------------------------------Label & Entry----------------------------------------------------

        lbl_cust_ref = Label(labelframeright, text="Enter the message:", font=("serif", 13), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeright, font=("arial", 13, "bold"),)
        entry_ref.place(x=150,y=12,width=400,height=300)

        # ---------------------------------------Submit Button------------------------
        btn_frame = Frame(labelframeright, bd=2, relief=RIDGE)
        btn_frame.place(x=720, y=12, width=200, height=40)

        btnAdd = Button(labelframeright, text="Send Review", font=("arial", 12, "bold"), bg="black", fg="gold", cursor="hand1", width=9)
        btnAdd.place(x=790,y=260,width=200,height=50)

        # ------------------------------------------email---------------------------------------------
        lbl_email = Label(labelframeright, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.place(x=750,y=100)
        entry_email = Entry(labelframeright, width=29, font=("arial", 13, "bold"))
        entry_email.place(x=820,y=100,width=300,height=40)

        # ------------------------------------------name---------------------------------------------
        lbl_name = Label(labelframeright, text="Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_name.place(x=750,y=20)
        entry_name = Entry(labelframeright, width=29, font=("arial", 13, "bold"))
        entry_name.place(x=820,y=20,width=300,height=40)





if __name__ == '__main__':
    root=Tk()
    obj=Report_Win(root)
    root.mainloop()