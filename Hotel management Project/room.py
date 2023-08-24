from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1240x510+300+280")

        # -----------------------------------------variables----------------------------------------------------------------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        # -----------------------------------------TITLE-------------------------------------------------------------------
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 30, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1550, height=40)

        # -------------------------------------------LOGO------------------------------------------------------------------
        img_logo = Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\grandBay.jpg")
        img_logo = img_logo.resize((100, 40))
        self.photologo = ImageTk.PhotoImage(img_logo)
        lblimg = Label(self.root, image=self.photologo, border=1, relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=40)

        # -----------------------------------------LabelFrame---------------------------------------------------------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", padx=2,font=("new times roman", 12, "bold"))
        labelframeleft.place(x=5, y=40, width=425, height=450)


        # ------------------------------------------Label & Entry----------------------------------------------------

        #customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        # Fetch Data Button
        btnFetch = Button(labelframeleft,command=self.Fetch_contact, text="Fetch Data",font=("arial", 8, "bold"), bg="black", fg="gold",cursor="hand1", width=9)
        btnFetch.place(x=340,y=4)

        #Check_in Date
        check_in_date = Label(labelframeleft, text="Check_in Date:", font=("arial", 12, "bold"), padx=2,pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheckin_date= ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"))
        txtcheckin_date.grid(row=1, column=1)

        # Check_out Date
        check_out_date = Label(labelframeleft, text="Check_Out Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheckout_date = ttk.Entry(labelframeleft,textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"))
        txtcheckout_date.grid(row=2, column=1)

        # Room Type
        label_RoomType = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomavailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        txtRoomavailable.grid(row=4,column=1)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft,textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(labelframeleft, text="No of Days:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblNoOfDays = Label(labelframeleft, text="Paid Tax:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=7, column=1)

        # Sub Total
        lblNoOfDays = Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=8, column=1)

        # Total cost
        lblIdNumber = Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_total, font=("arial", 13, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        # -----------------------------------------Bill Buttons-----------------------------------------------------------
        btnBill=Button(labelframeleft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",cursor="hand1",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        # -------------------------------------------------------buttons---------------------------------------------------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=8, y=390, width=400, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data,font=("arial", 12, "bold"), bg="black", fg="gold",cursor="hand1", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black",fg="gold", cursor="hand1", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 12, "bold"), bg="black",fg="gold", cursor="hand1", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 12, "bold"), bg="black",fg="gold", cursor="hand1", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # --------------------------------------------------------RightSide image---------------------------------------------------------
        img3 = Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\downimg2.jpg")
        img3 = img3.resize((450, 250))
        self.photoimg = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg, border=1, relief=RIDGE)
        lblimg.place(x=760, y=55, width=450, height=250)
        # -----------------------------------------------------tableframe search system ----------------------------------------------------

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",font=("arial", 12, "bold"))
        Table_Frame.place(x=440, y=280, width=1000, height=460)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="gold", fg="black")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24,state="readonly", cursor="hand2")
        combo_search["value"] = ("Contact", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=4)

        self.txt_search = StringVar()
        txtidNumber = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=29)
        txtidNumber.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search,font=("arial", 11, "bold"), bg="black",fg="gold", cursor="hand2")
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data,font=("arial", 11, "bold"),bg="black", fg="gold", cursor="hand2")
        btnShowAll.grid(row=0, column=4, padx=1)

        # --------------------------------------------show data table--------------------------------------------------------

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=3, y=50, width=750, height=350)

        scrollx = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("contact", "checkinDate", "checkoutDate", "roomtype", "roomavailable", "meal", "noOfdays"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.room_table.xview)
        scrolly.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkinDate", text="Check-in")
        self.room_table.heading("checkoutDate", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")


        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkinDate", width=100)
        self.room_table.column("checkoutDate", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("error","All fields are required",parent=self.root)
        else:
            try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Dshetty26#",database="sys")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                 self.var_contact.get(),
                                                                                 self.var_checkin.get(),
                                                                                 self.var_checkout.get(),
                                                                                 self.var_roomtype.get(),
                                                                                 self.var_roomavailable.get(),
                                                                                 self.var_meal.get(),
                                                                                 self.var_noofdays.get(),
                                                                             ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

     # =========================================FETCH DATA-----------------------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_rows=self.room_table.focus()
        content=self.room_table.item(cursor_rows)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])


# -----------------------------------All Data Fetch-------------------------------------------------------
    def Fetch_contact(self):
        if self.var_contact.get()=="":
          messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
          conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
          my_cursor = conn.cursor()
          query=("select Name from customer where Mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          if row==None:
            messagebox.showerror("Error","This Number not Found",parent=self.root)
          else:
            conn.commit()
            conn.close()

            showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataFrame.place(x=455,y=55,width=300,height=200)

            lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)

            lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
            lbl.place(x=80,y=0)

            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            query = ("select Gender from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblGender = Label(showDataFrame, text="Gender:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=30)

            lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
            lbl2.place(x=80, y=30)


            #---------------email------------------------------------------------------------
            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            query = ("select Email from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblEmail = Label(showDataFrame, text="Email:", font=("arial", 12, "bold"))
            lblEmail.place(x=0, y=60)

            lbl3 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
            lbl3.place(x=80, y=60)

            # ---------------------------------Nationality------------------------------------------------------------
            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            query = ("select Nationality from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblNationality = Label(showDataFrame, text="Nationality:", font=("arial", 12, "bold"))
            lblNationality.place(x=0, y=90)

            lbl4 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
            lbl4.place(x=90, y=90)

            # --------------- Address------------------------------------------------------------
            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            query = ("select Address from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblAddress = Label(showDataFrame, text="Address:", font=("arial", 12, "bold"))
            lblAddress.place(x=0, y=120)

            lbl5 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
            lbl5.place(x=90, y=120)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def update(self):
        if self.var_checkin.get()=="":
            messagebox.showerror("Error","Please enter check-in date!",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check-out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfDays=%s where Contact=%s",(
                                                                                                                                                                    self.var_checkin.get(),
                                                                                                                                                                    self.var_checkout.get(),
                                                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                                                    self.var_meal.get(),
                                                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()

