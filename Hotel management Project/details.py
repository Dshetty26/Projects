from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Details_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1240x510+300+280")


        # -------------------------------------------LOGO------------------------------------------------------------------
        img_logo = Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\grandBay.jpg")
        img_logo = img_logo.resize((120, 60))
        self.photologo = ImageTk.PhotoImage(img_logo)
        lblimg = Label(self.root, image=self.photologo, border=1, relief=RIDGE)
        lblimg.place(x=400, y=0, width=200, height=60)


        # -----------------------------------------------------labelframe search system ----------------------------------------------------

        labelframeright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("arial", 12, "bold"))
        labelframeright.place(x=15, y=60, width=1200, height=450)
        # --------------------------------------------show data table--------------------------------------------------------

        details_table = Frame(labelframeright, bd=2, relief=RIDGE)
        details_table.place(x=3, y=50, width=1100, height=350)

        scrollx = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_Details_table = ttk.Treeview(details_table, column=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.cust_Details_table.xview)
        scrolly.config(command=self.cust_Details_table.yview)

        self.cust_Details_table.heading("ref", text="Refer No")
        self.cust_Details_table.heading("name", text="Name")
        self.cust_Details_table.heading("mother", text="Mother")
        self.cust_Details_table.heading("gender", text="Gender")
        self.cust_Details_table.heading("post", text="Post")
        self.cust_Details_table.heading("mobile", text="Mobile")
        self.cust_Details_table.heading("email", text="Email")
        self.cust_Details_table.heading("nationality", text="Nationality")
        self.cust_Details_table.heading("idproof", text="ID Proof")
        self.cust_Details_table.heading("idnumber", text="ID Number")
        self.cust_Details_table.heading("address", text="Address")

        self.cust_Details_table["show"] = ["headings"]

        self.cust_Details_table.column("ref", width=100)
        self.cust_Details_table.column("name", width=100)
        self.cust_Details_table.column("mother", width=100)
        self.cust_Details_table.column("gender", width=100)
        self.cust_Details_table.column("post", width=100)
        self.cust_Details_table.column("mobile", width=100)
        self.cust_Details_table.column("email", width=100)
        self.cust_Details_table.column("nationality", width=100)
        self.cust_Details_table.column("idproof", width=100)
        self.cust_Details_table.column("idnumber", width=100)
        self.cust_Details_table.column("address", width=100)

        self.cust_Details_table.pack(fill=BOTH, expand=1)
        self.cust_Details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

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



if __name__ == '__main__':
    root=Tk()
    obj=Details_Win(root)
    root.mainloop()
