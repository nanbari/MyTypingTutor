
from tkinter import *

def text_exercise_page(wind):
#Function used to go to Text Exercise
    from MyTypingTutorTextExercise import create_exercices_window
    wind.destroy()
    window = create_exercices_window()
    window.mainloop()

def create_instructions_window():
#Creating Window for instructions
    instructions_window = Tk()
    instructions_window.resizable(0,0)
    instructions_window.attributes('-topmost', True)
    instructions_window.title("MyTypingTutor  -  Text Exercises Instructions")

    instructions = Label (instructions_window, text="Type the following text as quickly as possible. You will be timed. Press on the 'Start' button to start the timer. When you finish, press the 'Finish' button.",wraplength=370, font=("Times New Roman",14), padx=30,pady=10, justify=CENTER)
    instructions.grid()

    #Creating Button to go to Text Exercise
    text_exercise_button = Button( instructions_window,  text="Go To Text Exercise",  command=lambda: text_exercise_page(instructions_window))
    text_exercise_button.grid(padx=30, pady=20) 

    return instructions_window