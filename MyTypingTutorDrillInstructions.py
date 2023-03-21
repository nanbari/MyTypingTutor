
from tkinter import *

def word_drill_page(wind):
#Function used to go to Word Drill

    wind.destroy()
    from MyTypingTutorWordDrill import create_word_drill_window
    window = create_word_drill_window()
    window.mainloop()

def create_drill_intruction_window():
    #Creating window displaying Word Drill instructions
    instructions_window = Tk()
    instructions_window.resizable(0,0)
    instructions_window.attributes('-topmost', True)
    instructions_window.title("MyTypingTutor  -  Word Drill Instructions")


    instructions = Label (instructions_window, text="The following words are the words you need to pratice. Type the word displayed as quickly as possible, and then press enter.",wraplength=370, font=("Times New Roman",14), padx=30,pady=10, justify=CENTER)
    instructions.grid()
    
    #Creating Button to go to Word Drill
    word_drill_button = Button( instructions_window,  text="Go To Word Drill",  command=lambda: word_drill_page(instructions_window))
    word_drill_button.grid(padx=30, pady=20) 

    return instructions_window