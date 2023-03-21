from sre_parse import State
from tkinter import *
from Timing import Timing



def main_menu_page(exercise_wind):
# function used to go to the Main Menu 
    from MyTypingTutorMainMenu import create_main_menu_window
    exercise_wind.destroy()
    window = create_main_menu_window()
    window.mainloop()
    

def create_exercices_window():
    #The Text Exercise window is created
    exercise_window = Tk()
    exercise_window.resizable(0,0)
    exercise_window.title("MyTypingTutor  -  Text Exercises")

    #Creating mainframe inside window
    main_frame = Frame(exercise_window)
    main_frame.grid()

    #Creating paragraph_frame inside mainframe and wrinting paragraph ( which is the text that should be typed by the user)
    paragraph_frame = Frame(main_frame, pady=7, bd = 7 )
    paragraph_frame.grid(row = 2, column = 0)

    text_to_be_typed="One-third of a medium avocado (50 g) has 80 calories and contributes nearly 20 vitamins and minerals, making it a nutrient-dense choice."

    paragraph = Label (paragraph_frame, borderwidth=2, relief="solid", text=text_to_be_typed , wraplength = 720, justify=LEFT, font=("Times New Roman",13))
    paragraph.grid(ipadx=7, ipady=7)

    #Creating text_frame inside mainframe and creating entry ( which is the area where the user should enter the text)
    text_frame = Frame (main_frame, pady= 3)
    text_frame.grid(row=3, column = 0) 

    entry = Text(text_frame, font=('Times New Roman', 12, 'bold'), width= 90, height= 7, wrap='word', state=DISABLED)
    entry.grid()

    # Creating start Button 

    timing = Timing(main_frame, entry, text_to_be_typed)
    timing.Buttons()

    

    # Creating Button to go to the Main Menu
    main_menu_button = Button( timing.button_frame,  text="Main Menu",  command= lambda: main_menu_page(exercise_window))
    main_menu_button.grid(row = 0, column= 3, padx= 10 ) 

    
    def display_keyboard():
        #Creating window displaying keyboard
        keyboard_window = Tk()
        keyboard_window.resizable(0,0)
        keyboard_window.attributes('-topmost', True)
        keyboard_window.title('MyTyping Tutor  -  Keyboard')

        # Creating the keyboard 
        numbers_row = Frame(keyboard_window)
        numbers_row.grid(pady=3)

        number1 = Label(numbers_row, text = "1", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number2 = Label(numbers_row, text = "2", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number3 = Label(numbers_row, text = "3", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number4 = Label(numbers_row, text = "4", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number5 = Label(numbers_row, text = "5", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number6 = Label(numbers_row, text = "6", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number7 = Label(numbers_row, text = "7", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number8 = Label(numbers_row, text = "8", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number9 = Label(numbers_row, text = "9", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number0 = Label(numbers_row, text = "0", bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        number1.grid(row=0,column=0,padx=3)
        number2.grid(row=0,column=1,padx=3)
        number3.grid(row=0,column=2,padx=3)
        number4.grid(row=0,column=3,padx=3)
        number5.grid(row=0,column=4,padx=3)
        number6.grid(row=0,column=5,padx=3)
        number7.grid(row=0,column=6,padx=3)
        number8.grid(row=0,column=7,padx=3)
        number9.grid(row=0,column=8,padx=3)
        number0.grid(row=0,column=9,padx=3)

        first_letter_row = Frame(keyboard_window)
        first_letter_row.grid(row=1, column=0, pady=3)

        letterQ = Label(first_letter_row, text='Q', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterW = Label(first_letter_row, text='W', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterE = Label(first_letter_row, text='E', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterR = Label(first_letter_row, text='R', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterT = Label(first_letter_row, text='T', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterY = Label(first_letter_row, text='Y', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterU = Label(first_letter_row, text='U', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterI = Label(first_letter_row, text='I', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterO = Label(first_letter_row, text='O', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)
        letterP = Label(first_letter_row, text='P', bg= 'grey',fg= 'white', font=('Times New Roman',12,'bold'),width=4, height=2, relief=RAISED, bd=5)

        letterQ.grid(row=0,column=1,padx=3)
        letterW.grid(row=0,column=2,padx=3)
        letterE.grid(row=0,column=3,padx=3)
        letterR.grid(row=0,column=4,padx=3)
        letterT.grid(row=0,column=5,padx=3)
        letterY.grid(row=0,column=6,padx=3)
        letterU.grid(row=0,column=7,padx=3)
        letterI.grid(row=0,column=8,padx=3)
        letterO.grid(row=0,column=9,padx=3)
        letterP.grid(row=0,column=10,padx=3)

        second_letter_row=Frame(keyboard_window)
        second_letter_row.grid(row=2,column=0, pady=3)
        
        letterA=Label(second_letter_row,text='A',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterS=Label(second_letter_row,text='S',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterD=Label(second_letter_row,text='D',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterF=Label(second_letter_row,text='F',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterG=Label(second_letter_row,text='G',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterH=Label(second_letter_row,text='H',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterJ=Label(second_letter_row,text='J',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterK=Label(second_letter_row,text='K',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterL=Label(second_letter_row,text='L',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)

        letterA.grid(row=0,column=0,padx=3)
        letterS.grid(row=0,column=1,padx=3)
        letterD.grid(row=0,column=2,padx=3)
        letterF.grid(row=0,column=3,padx=3)
        letterG.grid(row=0,column=4,padx=3)
        letterH.grid(row=0,column=5,padx=3)
        letterJ.grid(row=0,column=6,padx=3)
        letterK.grid(row=0,column=7,padx=3)
        letterL.grid(row=0,column=8,padx=3)

        third_letter_row=Frame(keyboard_window)
        third_letter_row.grid(row=3,column=0,pady=3)

        letterZ=Label(third_letter_row,text='Z',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterX=Label(third_letter_row,text='X',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterC=Label(third_letter_row,text='C',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterV=Label(third_letter_row,text='V',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterB=Label(third_letter_row,text='B',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterN=Label(third_letter_row,text='N',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)
        letterM=Label(third_letter_row,text='M',bg='grey',fg='white',font=('Times New Roman',12,'bold'),width=4,height=2,bd=5,relief=RAISED)

        letterZ.grid(row=0,column=0,padx=3)
        letterX.grid(row=0,column=1,padx=3)
        letterC.grid(row=0,column=2,padx=3)
        letterV.grid(row=0,column=3,padx=3)
        letterB.grid(row=0,column=4,padx=3)
        letterN.grid(row=0,column=5,padx=3)
        letterM.grid(row=0,column=6,padx=3)

        space=Frame(keyboard_window)
        space.grid(row=4,column=0,pady=3)

        label_space=Label(space,bg='grey',fg='white',width=40,height=2,bd=10,relief=RAISED)
        label_space.grid()

        

                                    

    # Creating button to display the keyboard window
    display_keyboard_button = Button( timing.button_frame,  text="Show Keyboard",  command= display_keyboard )
    display_keyboard_button.grid(row = 0, column= 4, padx= 10) 

    return exercise_window