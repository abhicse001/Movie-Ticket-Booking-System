from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



win=Tk()
win.geometry("900x700")
win.title("Ticket booking system ")



def register():
    def click_register():
        id=entry_id.get()
        name=entry_name.get()
        email=entry_email.get()
        psw=entry_password.get()
        contact=entry_contact.get()

        if (id=="" or psw=="" or name=="" or email=="" or contact==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        else:
            con=mysql.connect(host="localhost",user="root",password="Abhishek123@#",database="ticket_book",auth_plugin='mysql_native_password')
            cursor=con.cursor()
            cursor.execute("insert into registration values('"+id+"','"+name+"','"+email+"','"+contact+"','"+psw+"')")
            cursor.execute("commit")

            MessageBox.showinfo("Alert","Registration completed Successfully")
            con.close()
            login()

    f1=Frame(bg="#0096DC")
    f1.place(x=0,y=0,height=500,width=500)

    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l2=Label(f1,text="Name:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l3=Label(f1,text="Email",font=("Verdena 15"),fg="white",bg="#0096DC")
    l4=Label(f1,text="Contact",font=("Verdena 15"),fg="white",bg="#0096DC")
    l5=Label(f1,text="Password:",font=("Verdena 15"),fg="white",bg="#0096DC")

    l1.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=0)
    l4.grid(row=3,column=0)
    l5.grid(row=4,column=0)

    entry_id=Entry(f1,font=("Verdena 15"))
    entry_name=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_contact=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,show="*",font=("Verdena 15"))
    
    entry_id.grid(row=0,column=1)
    entry_name.grid(row=1,column=1)
    entry_email.grid(row=2,column=1)
    entry_password.grid(row=3,column=1)
    entry_contact.grid(row=4,column=1)


    b1=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="grey",command=click_register)
    b2=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="grey",command=login)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)
    
    
    
def login():
    def click_login():
        id=entry_id.get()
        email=entry_email.get()
        psw=entry_password.get()
        
        con=mysql.connect(host="localhost",user="root",password="Abhishek123@#",database="ticket_book")
        cursor=con.cursor()
        cursor.execute("SELECT Userid FROM registration")
        database_id=cursor.fetchall()
        cursor.execute("SELECT Email FROM registration")
        database_email=cursor.fetchall()
        cursor.execute("SELECT Password FROM registration")
        database_psw=cursor.fetchall()
        
        
        var1=0
        var2=0
        var3=0

        
        for userid in database_id:
               uid=userid[0]
               if(uid==id):
                   var1=1    
        for useremail in database_email:
               uml=useremail[0]
               if(uml==email):
                   var2=1    
        for userpsw in database_psw:
               upw=userpsw[0]
               if(upw==psw):
                   var3=1    
          
        if (id=="" or psw=="" or email==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        elif(var1==1 or var2==1 or var3==1):
            MessageBox.showinfo("Alert","Login completed Successfully")
            




        # tk=Frame(bg="aqua")
        # tk.place(x=0,y=0,width=500,height=600)
        # tk.geometry("500x400")

            #
        class MovieBookingApp:
            def __init__(self, root):
                # con=mysql.connect(host="localhost",user="root",password="Abhishek123@#",database="ticket_book")
                # cursor=con.cursor()
                # cursor.execute("SELECT Select Movie FROM movie")
                # database_id=cursor.fetchall()
                # cursor.execute("SELECT Select Venue FROM movie")
                # database_email=cursor.fetchall()
                # cursor.execute("SELECT Select Date and Time FROM movie")
                # database_psw=cursor.fetchall()
                # cursor.execute("SELECT  Payment Method FROM movie")
                # database_psw=cursor.fetchall()
                # con.commit()
                # con.close()

        


                self.root = root
                self.root.title("Movie Ticket Booking System")
                self.root.geometry("500x400")
                self.root.configure(bg="#f0f0f0")

                self.create_widgets()



            def create_widgets(self):
                # Movie selection
                tk.Label(self.root, text="Select Movie:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
                self.movie_var = tk.StringVar()
                self.movie_dropdown =ttk.Combobox(self.root, textvariable=self.movie_var, font=("Arial", 10))
                self.movie_dropdown['values'] = ["Movie 1", "Movie 2", "Movie 3"]
                self.movie_dropdown.pack(pady=5)

                # Venue selection
                tk.Label(self.root, text="Select Venue:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
                self.venue_var = tk.StringVar()
                self.venue_dropdown = ttk.Combobox(self.root, textvariable=self.venue_var, font=("Arial", 10))
                self.venue_dropdown['values'] = ["Venue 1", "Venue 2", "Venue 3"]
                self.venue_dropdown.pack(pady=5)

                # Date and time selection
                tk.Label(self.root, text="Select Date and Time:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
                self.date_var = tk.StringVar()
                self.time_var = tk.StringVar()
                self.date_entry = tk.Entry(self.root, textvariable=self.date_var, font=("Arial", 10))
                self.time_entry = tk.Entry(self.root, textvariable=self.time_var, font=("Arial", 10))
                self.date_entry.pack(pady=5)
                self.time_entry.pack(pady=5)

                # Payment method
                tk.Label(self.root, text="Payment Method:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
                self.payment_var = tk.StringVar()
                self.payment_options = ttk.Combobox(self.root, textvariable=self.payment_var, font=("Arial", 10))
                self.payment_options['values'] = ["Credit Card", "Debit Card", "PayPal"]
                self.payment_options.pack(pady=5)

                # Submit button
                self.submit_button = tk.Button(self.root, text="Book Now", command=self.book_ticket, font=("Arial", 12), bg="#4CAF50", fg="white")
                self.submit_button.pack(pady=20)

            def book_ticket(self):
                movie = self.movie_var.get()
                venue = self.venue_var.get()
                date = self.date_var.get()
                time = self.time_var.get()
                payment = self.payment_var.get()

                if not all([movie, venue, date, time, payment]):
                    messagebox.showerror("Error", "All fields must be filled!")
                else:
                    messagebox.showinfo("Success", "Booking successful!")

        if __name__ == "__main__":
            root = tk.Tk()
            app = MovieBookingApp(root)
            root.mainloop()

                    
           
        else:
            MessageBox.showinfo("Alert","There is error")

        
    f1=Frame(bg="cyan")
    f1.place(x=0,y=0,height=500,width=500)
    
    label_head=Label(f1,text="Fill credentials To Login",font=("Verdena 25"),fg="white",bg="#B1DDC6")
    label_head.place(x=80,y=10)
    
    
    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    l2=Label(f1,text="Email",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    l3=Label(f1,text="password",font=("Verdena 15"),fg="white",bg="#B1DDC6")
    
    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    
    entry_id=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,font=("Verdena 15"),show="*")

    entry_id.place(x=200,y=100)
    entry_email.place(x=200,y=150)
    entry_password.place(x=200,y=200)
    
    b1=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="grey",command=click_login)
    b2=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="grey",command=register)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)
register()
win.mainloop()


