from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1240x510+300+280")


# --------------------------------------------------------Variable for storing data---------------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_mother=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_post=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_nationality=StringVar()
        self.var_cust_address=StringVar()
        self.var_cust_id_proof=StringVar()
        self.var_cust_id_number=StringVar()
        self.var_cust_address=StringVar()

# -----------------------------------------TITLE-------------------------------------------------------------------
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=40)

# -------------------------------------------LOGO------------------------------------------------------------------
        img_logo = Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\HotelName.png")
        img_logo = img_logo.resize((200, 40))
        self.photologo = ImageTk.PhotoImage(img_logo)
        lblimg = Label(self.root, image=self.photologo, border=1, relief=RIDGE)
        lblimg.place(x=0, y=0, width=200, height=40)


# -----------------------------------------LabelFrame---------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",padx=2,font=("new times roman",12,"bold"))
        labelframeleft.place(x=5,y=40,width=425,height=450)


# ------------------------------------------Label & Entry----------------------------------------------------
        #customer reference
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)


        #customer name
        lbl_name=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_name.grid(row=1,column=0,sticky=W)

        entry_name=Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        entry_name.grid(row=1,column=1)

        #mother name
        lbl_name = Label(labelframeleft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_name.grid(row=2, column=0, sticky=W)

        entry_name = Entry(labelframeleft,textvariable=self.var_cust_mother, width=29, font=("arial", 13, "bold"))
        entry_name.grid(row=2, column=1)

        #gender combobox
        lbl_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_cust_gender,font=("arial", 12, "bold"),width=27,state="readonly",cursor="hand2")
        combo_gender["value"]=["Male","Female","Other"]
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #postcode
        lbl_postcode = Label(labelframeleft, text="PostCode:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)
        entry_postcode = Entry(labelframeleft,textvariable=self.var_cust_post, width=29, font=("arial", 13, "bold"))
        entry_postcode.grid(row=4, column=1)

        #Mobile number
        lbl_mobileno = Label(labelframeleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobileno.grid(row=5, column=0, sticky=W)
        entry_mobile = Entry(labelframeleft,textvariable=self.var_cust_mobile, width=29, font=("arial", 13, "bold"))
        entry_mobile.grid(row=5, column=1)

        #email
        lbl_email = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)
        entry_email = Entry(labelframeleft,textvariable=self.var_cust_email, width=29, font=("arial", 13, "bold"))
        entry_email.grid(row=6, column=1)

        #Nationality combobox
        lbl_nationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=7, column=0, sticky=W)

        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_cust_nationality,font=("arial", 12, "bold"),width=27,state="readonly",cursor="hand2")
        combo_nationality["value"]=["Indian","NRI","Other"]
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        #Id proof combobox
        lbl_idproof = Label(labelframeleft, text="Id Proof type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_idproof.grid(row=8, column=0, sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_cust_id_proof,font=("arial", 12, "bold"),width=27,state="readonly",cursor="hand2")
        combo_id["value"]=["Adharcard","Driving License","Pancard","Passport"]
        combo_id.current(0)
        combo_id.grid(row=8,column=1)


        #Id Number
        lbl_idnumber = Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_idnumber.grid(row=9, column=0, sticky=W)
        entry_idnumber = Entry(labelframeleft, textvariable=self.var_cust_id_number,width=29, font=("arial", 13, "bold"))
        entry_idnumber.grid(row=9, column=1)

        #Address
        lbl_address = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)
        entry_address = Entry(labelframeleft,textvariable=self.var_cust_address, width=29, font=("arial", 13, "bold"))
        entry_address.grid(row=10, column=1)

# -------------------------------------------------------buttons---------------------------------------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=8,y=390,width=400,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",cursor="hand1",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", cursor="hand1",width=9)
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", cursor="hand1",width=8)
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", cursor="hand1",width=9)
        btnReset.grid(row=0, column=3,padx=1)

# -----------------------------------------------------labelframe search system ----------------------------------------------------

        labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"))
        labelframeright.place(x=440,y=50,width=1000,height=600)

        lblSearchBy=Label(labelframeright,font=("arial",12,"bold"),text="Search By:",bg="gold",fg="black")
        lblSearchBy.grid(row=0,column=0,sticky=W)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(labelframeright,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly",cursor="hand2")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=4)

        self.txt_search=StringVar()
        txtidNumber=ttk.Entry(labelframeright,textvariable=self.txt_search,font=("arial",13,"bold"),width=29)
        txtidNumber.grid(row=0,column=2,padx=4)

        btnSearch=Button(labelframeright,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",cursor="hand2")
        btnSearch.grid(row=0,column=3,padx=2)

        btnShowAll=Button(labelframeright,text="Show All",command=self.fetch_data,font=("arial", 11,"bold"),bg="black",fg="gold",cursor="hand2")
        btnShowAll.grid(row=0,column=4,padx=2)




# --------------------------------------------show data table--------------------------------------------------------

        details_table=Frame(labelframeright,bd=2,relief=RIDGE)
        details_table.place(x=3,y=50,width=750,height=350)

        scrollx=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_Details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.cust_Details_table.xview)
        scrolly.config(command=self.cust_Details_table.yview)

        self.cust_Details_table.heading("ref",text="Refer No")
        self.cust_Details_table.heading("name",text="Name")
        self.cust_Details_table.heading("mother",text="Mother")
        self.cust_Details_table.heading("gender",text="Gender")
        self.cust_Details_table.heading("post",text="Post")
        self.cust_Details_table.heading("mobile",text="Mobile")
        self.cust_Details_table.heading("email",text="Email")
        self.cust_Details_table.heading("nationality",text="Nationality")
        self.cust_Details_table.heading("idproof",text="ID Proof")
        self.cust_Details_table.heading("idnumber",text="ID Number")
        self.cust_Details_table.heading("address",text="Address")

        self.cust_Details_table["show"]=["headings"]

        self.cust_Details_table.column("ref",width=100)
        self.cust_Details_table.column("name",width=100)
        self.cust_Details_table.column("mother",width=100)
        self.cust_Details_table.column("gender",width=100)
        self.cust_Details_table.column("post",width=100)
        self.cust_Details_table.column("mobile",width=100)
        self.cust_Details_table.column("email",width=100)
        self.cust_Details_table.column("nationality",width=100)
        self.cust_Details_table.column("idproof",width=100)
        self.cust_Details_table.column("idnumber",width=100)
        self.cust_Details_table.column("address",width=100)

        self.cust_Details_table.pack(fill=BOTH,expand=1)
        self.cust_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


# ------------------------------------------------Adding Data into MySQL--------------------------
    def add_data(self):
        if self.var_cust_name.get()=="" or self.var_cust_mobile.get()=="" or self.var_cust_id_number.get()=="":
          messagebox.showerror("error","All fields are required",parent=self.root)
        else:
            try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Dshetty26#",database="sys")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get()
                                                                                           ,self.var_cust_name.get()
                                                                                           ,self.var_cust_mother.get()
                                                                                           ,self.var_cust_gender.get()
                                                                                           ,self.var_cust_post.get()
                                                                                           ,self.var_cust_mobile.get()
                                                                                           ,self.var_cust_email.get()
                                                                                           ,self.var_cust_nationality.get()
                                                                                           ,self.var_cust_id_proof.get()
                                                                                           ,self.var_cust_id_number.get()
                                                                                           ,self.var_cust_address.get()
                                                                                           ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_table.delete(*self.cust_Details_table.get_children())
            for i in rows:
                self.cust_Details_table.insert("",END,values=i)
            conn.commit()
        conn.close()




    def get_cursor(self,event=""):
        cursor_rows=self.cust_Details_table.focus()
        content=self.cust_Details_table.item(cursor_rows)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_cust_mother.set(row[2]),
        self.var_cust_gender.set(row[3]),
        self.var_cust_post.set(row[4]),
        self.var_cust_mobile.set(row[5]),
        self.var_cust_email.set(row[6]),
        self.var_cust_nationality.set(row[7]),
        self.var_cust_id_proof.set(row[8]),
        self.var_cust_id_number.set(row[9]),
        self.var_cust_address.set(row[10])


    def update(self):
        if self.var_cust_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,IDproof=%s,IDnumber=%s,Address=%s where Ref=%s",(

                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                    self.var_cust_mother.get(),
                                                                                                                                                                    self.var_cust_gender.get(),
                                                                                                                                                                    self.var_cust_post.get(),
                                                                                                                                                                    self.var_cust_mobile.get(),
                                                                                                                                                                    self.var_cust_email.get(),
                                                                                                                                                                    self.var_cust_nationality.get(),
                                                                                                                                                                    self.var_cust_id_proof.get(),
                                                                                                                                                                    self.var_cust_id_number.get(),
                                                                                                                                                                    self.var_cust_address.get(),
                                                                                                                                                                    self.var_ref.get()
                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_cust_mother.set(""),
        # self.var_cust_gender.set(""),
        self.var_cust_post.set(""),
        self.var_cust_mobile.set(""),
        self.var_cust_email.set(""),
        # self.var_cust_nationality.set(""),
        # self.var_cust_id_proof.set(""),
        self.var_cust_id_number.set(""),
        self.var_cust_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Dshetty26#", database="sys")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_table.delete(*self.cust_Details_table.get_children())
            for i in rows:
                self.cust_Details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
 



if __name__ == '__main__':
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
