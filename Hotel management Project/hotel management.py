from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking
from report import Report_Win
from details import Details_Win

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry('1550x800+0+0')

# ---------------------------------------Hotel Image----------------------------------------------------------

        img1=Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\hotelmain3.jpeg")
        img1=img1.resize((1245,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,border=4,relief=RIDGE)
        lblimg.place(x=300,y=0,width=1245,height=200)

# ---------------------------------------Hotel Name----------------------------------------------------------

        img2=Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\grandBay.jpg")
        img2=img2.resize((300,200))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,border=2,relief=RIDGE)
        lblimg.place(x=0,y=0,width=300,height=200)

# ------------------------------------------Hotel Bar-----------------------------------------------------------

        # img3=Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\hotelmain3.jpeg")
        # img3=img3.resize((245,200))
        # self.photoimg3=ImageTk.PhotoImage(img3)
        # lblimg=Label(self.root,image=self.photoimg3,border=2,relief=RIDGE)
        # lblimg.place(x=1300,y=0,width=210,height=200)
#         img3 = Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\hotelmain3.jpeg")
#         img3 = img3.resize((230, 200))
#         self.photoimg3 = ImageTk.PhotoImage(img3)
#         lblimg=Label(self.root,image=self.photoimg3, border=2, relief=RIDGE)                    #image=self.photoimg3
#         lblimg.place(x=300, y=0, width=230, height=200)
# ---------------------------------------Hotel Title----------------------------------------------------------

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_title.place(x=0,y=200,width=1550,height=50)


# ---------------------------------------Hotel Frame----------------------------------------------------------
        main_frame=Frame(self.root,bd=2,relief=RIDGE)
        main_frame.place(x=0,y=250,width=1550,height=550)

# ---------------------------------------Hotel Menu----------------------------------------------------------
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=300)


# ---------------------------------------Button Frame----------------------------------------------------------
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=300,height=215)

        cust_button=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=24,font=("times new roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_button.grid(row=0,column=0,pady=1)

        room_button=Button(btn_frame,text="ROOM",command=self.roombooking,width=24,font=("times new roman", 15, "bold"),bg="black",fg="gold", cursor="hand2")
        room_button.grid(row=1, column=0, pady=1)

        details_button=Button(btn_frame,text="DETAILS",command=self.roomBooking_details,width=24,font=("times new roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        details_button.grid(row=2, column=0, pady=1)

        report_button=Button(btn_frame,text="REPORT",command=self.report_details,width=24,font=("times new roman",15,"bold"), bg="black",fg="gold",cursor="hand2")
        report_button.grid(row=3, column=0, pady=1)

        logout_button=Button(btn_frame,text="LOGOUT",width=24,font=("times new roman",15,"bold"),bg="black",fg="gold",cursor="hand2")
        logout_button.grid(row=4, column=0, pady=1)


# -----------------------------------------------Hotel Dining Area------------------------------------------------

        img3=Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\DiningHall.png")
        img3=img3.resize((1250,550))
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(main_frame,image=self.photoimg3,border=2,relief=RIDGE)
        lblimg.place(x=300,y=0,width=1250,height=550)


# -----------------------------------------------Down Images------------------------------------------------

        img4=Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\downimg1.jpg")
        img4=img4.resize((300,150))
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(main_frame,image=self.photoimg4,border=1,relief=RIDGE)
        lblimg.place(x=0,y=250,width=300,height=150)

        img5 = Image.open(r"C:\Users\DESHIK SHETTY\Desktop\hotel managemet proj\pics\downimg2.jpg")
        img5 = img5.resize((300, 150))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg = Label(main_frame, image=self.photoimg5, border=1, relief=RAISED)
        lblimg.place(x=0, y=400, width=300, height=150)


# -------------------------------------------Customer Window---------------------------------------------------------

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def roomBooking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details_Win(self.new_window)

    def report_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Report_Win(self.new_window)


#         To call the object
if __name__ == '__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()



