from email import message
import email
import sqlite3
from tkinter import *
from typing import Literal
from Data import Data

Data.set_database(sqlite3.connect("users.db"))

cursor= Data.database

query = """
CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    mistakes TEXT 
);
"""
Data.database.execute(query)

class MySoftware:
    
    connected = False
    message = "" # Used later in create_account_window for error messages 
  
    @staticmethod 
    def go_to_menu(login_window):
        from MyTypingTutorMainMenu import create_main_menu_window
        login_window.destroy()
        window = create_main_menu_window()
        window.mainloop()
        

    def login(self,mail,passw,Frame, window):

        query = """
        SELECT * FROM users
        WHERE email=? AND password=?
        """
        cursor = Data.database.execute(query, (mail, passw))
        
        if len(cursor.fetchall()) != 0:
            self.connected = True
            Data.set_email_connected(mail)
            self.go_to_menu(window)
        else:
            error_label= Label(Frame, text='your password or email is incorrect', font=("Times New Roman",10,'bold'), fg='red')
            error_label.grid(row = 1)

        return None


    def register(self, mail, password1, password2, window):

        self.message.grid_forget()
        

        if password1 != password2 :
            mes ="Your passwords do not match"
            
        elif mail =="" or password1 =="":
            mes="email and password cannot be empty"
            
        else:
            query = """
            SELECT * FROM users
            WHERE email=? 
            """ 
            cursor = Data.database.execute(query, (mail,))
            if len(cursor.fetchall()) != 0:
                mes ="An account with this email address already exists"
                

            else:           
                query = """
                    INSERT INTO users (email, password, mistakes) VALUES
                    (?, ?," ")  
                    """
                cursor = Data.database.execute(query, (mail, password1))

                                         
                Data.database.commit()
                mes = "Your accout has been successfully created"

        self.message = Label(window, text=mes, font=("Times New Roman",10,'bold'), fg='black')
        self.message.grid(row= 1)        
         
        return None

    def create_login_page(self):

        #function creating the login window

        login_window = Tk()
        login_window.resizable(0,0)
        login_window.title("MyTypingTutor")

        # Creating Title 
        title_frame = Frame(login_window, pady=20, padx=20)
        title_frame.grid()

        title = Label( title_frame, text="Welcome to My Typing Tutor", font=("Times New Roman",15,'bold'))
        title.grid(padx=10, pady=10)

        title = Label( title_frame, text="Login to your account", font=("Times New Roman",13,'bold'))
        title.grid(row = 1, padx=10, pady=10)

        self.message=Label(login_window, text="") # Used later in create_account_window for error messages

        main_frame = Frame(login_window)
        main_frame.grid(row = 1, padx=10, pady=10)

        enteredemail = Entry(main_frame, width=30)
        enteredemail.grid(row = 0, column = 1, padx=10, pady=10)
        email_label = Label(main_frame, text ='Enter your email')
        email_label.grid(row =0, column = 0, padx=10, pady=10)

        enteredpassword= Entry(main_frame, width=30, show='*')
        enteredpassword.grid(row= 1 , column = 1, padx=10, pady=10)
        passwordLabel = Label(main_frame,text='Enter your password')
        passwordLabel.grid(row =1 , column = 0, padx=10, pady=10 )

        LoginBtn= Button(main_frame,text="Login", command=lambda: self.login(enteredemail.get(), enteredpassword.get(), title_frame, login_window))
        LoginBtn.grid(padx=10, pady=10)

        RegisterBtn = Button(main_frame,text="Create your account", command=lambda : self.create_account_window())
        RegisterBtn.grid(padx=10, pady=10)

    

        login_window.mainloop()

    def create_account_window(self):

        #function creating the create account window

        register_window = Tk()
        register_window.resizable(0,0)
        register_window.title("MyTypingTutor")

        # Creating Title
        title = Label( register_window, text="Create Your Account", font=("Times New Roman",15,'bold'))
        title.grid(padx=10, pady=10)

        # Creating emain and password fields
        emailentered = Entry(register_window, width=30)
        emailentered.grid(row = 2, column = 1, padx=10, pady=10)
        email_label = Label(register_window, text ='Enter your email')
        email_label.grid(row =2, column = 0, padx=10, pady=10)

        password1= Entry(register_window, width=30, show='*')
        password1.grid(row= 3 , column = 1, padx=10, pady=10)
        password1_label = Label(register_window, text='Enter your password')
        password1_label.grid(row =3, column = 0, padx=10, pady=10)

        password2= Entry(register_window, width=30, show='*')
        password2.grid(row= 4 , column = 1)
        password2_label = Label(register_window,text='Confirm your password')
        password2_label.grid(row =4, column = 0, padx=10, pady=10)

        #Creating button to create the account
        create_account_button = Button(register_window,text =" Create Your Account", command=lambda : self.register(emailentered.get(), password1.get(), password2.get(), register_window))
        create_account_button.grid(row = 5, padx=10, pady=10)

        register_window.mainloop()
        

if __name__ == "__main__": 
    software = MySoftware()
    software.create_login_page()
    
    
    






    
