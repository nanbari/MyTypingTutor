from tkinter import *
from tkinter import ttk



def text_exercise_page(main_menu_wind):
    # function used to go to Text Exercises 
    from MyTypingTutorExercicesInstructions import create_instructions_window
    main_menu_wind.destroy()
    window = create_instructions_window()
    window.mainloop()

def word_drill_page(wind):
    # function used to go to Word Drill 
    from MyTypingTutorDrillInstructions import create_drill_intruction_window
    wind.destroy()
    window = create_drill_intruction_window()
    window.mainloop()
            
def create_main_menu_window():
    #The main menu window is created
    main_menu_window = Tk()
    main_menu_window.resizable(0,0)
    main_menu_window.title("MyTypingTutor")

    # Creating Title 
    title_frame = Frame(main_menu_window, pady=20, padx=20)
    title_frame.grid()

    title = Label( title_frame, text="Welcome to My Typing Tutor", font=("Times New Roman",15,'bold'))
    title.grid()

    # Creating button to go to Text Exercises

    text_exercise_button = Button( main_menu_window,  text="Text Exercises",  command=lambda: text_exercise_page(main_menu_window))
    text_exercise_button.grid(padx=50) 

    # Creating button to go to Word Drill
    
    word_drill_button = Button( main_menu_window,  text="Word Drill",  command=lambda: word_drill_page(main_menu_window))
    word_drill_button.grid(padx=50, pady=15) 


    return main_menu_window
    
if __name__ == "__main__":

    window = create_main_menu_window()

    window.mainloop()