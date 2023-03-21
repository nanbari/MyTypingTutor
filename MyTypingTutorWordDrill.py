
from tkinter import *

from Data import Data


def main_menu_page(exercise_wind):
# Creating button to go to the Main Menu 
    from MyTypingTutorMainMenu import create_main_menu_window
    exercise_wind.destroy()
    window = create_main_menu_window()
    window.mainloop()


def create_word_drill_window():
    #The window is created
    word_drill_window = Tk()
    word_drill_window.resizable(0,0)
    word_drill_window.title("MyTypingTutor  -  Word Drill")

    #Getting mistakes of user from database
    query = """ SELECT mistakes
                    FROM Users 
                    WHERE email = ?;"""

    cursor= Data.database.execute(query,[Data.email_connected])
    mistakes_string= cursor.fetchone()[0]
    list_of_mistakes =mistakes_string.split()
     
    if list_of_mistakes == []:
        instructions = Label (word_drill_window, text="There are no problemtic words detected. Come back to this page once you have done the text exercises.",wraplength=370, font=("Times New Roman",14), padx=30,pady=10, justify=CENTER)
        instructions.grid()

        # Creating Button Frame 
        button_frame = Frame(word_drill_window, padx=15, pady=15)
        button_frame.grid(row=1, column =0)

        # Creating Button to go to the Main Menu
        main_menu_button = Button( button_frame,  text="Main Menu",  command= lambda: main_menu_page(word_drill_window))
        main_menu_button.grid(padx= 10 ) 

    else:

        
        #Creating MainFrame inside window
        main_frame = Frame(word_drill_window)
        main_frame.grid()

        #Creating paragraph_frame inside MainFrame and writing the word that should be typed by the user
        paragraph_frame = Frame(main_frame, pady=7, bd = 7 )
        paragraph_frame.grid(row = 2, column = 0)

        paragraph = Label (paragraph_frame, borderwidth=2, relief="solid", text=list_of_mistakes[0], wraplength = 720, justify=LEFT, font=("Times New Roman",13))
        paragraph.grid(ipadx=7, ipady=7)

        #Creating text_frame inside MainFrame and creating entry ( which is the area where the user should enter the text)
        text_frame = Frame (main_frame, pady= 3)
        text_frame.grid(row=3, column = 0)

        entry = Entry(text_frame, width= 50, font=("Times New Roman",13))
        entry.grid()

        #Creating Button Frame
        button_frame = Frame(main_frame, padx=15, pady=15)
        button_frame.grid(row=4, column =0) 

        #Creating Button to go to Main Menu
        main_menu_button = Button( button_frame,  text="Main Menu",  command= lambda: main_menu_page(word_drill_window))
        main_menu_button.grid(padx= 10 ) 

               
        def nextword(_):
            #This function changes the value of the word displayed (current_word) to the next word in list_of_mistakes once the user
            #enters the word correctly and presses enter. 
            current_word = list_of_mistakes[Data.drill_pos]
            if current_word == entry.get().strip():
                entry.delete(0, 'end')
                Data.set_drill_pos(Data.drill_pos + 1)
                if Data.drill_pos>= len(list_of_mistakes):
                    Data.set_drill_pos(0)
                    Data.set_drill_counter(Data.drill_counter + 1)
                current_word= list_of_mistakes[Data.drill_pos]

                paragraph.config(text=current_word)
                
        #binding nextword function execution to the <Return> event 
        entry.bind("<Return>", nextword)

    return word_drill_window
