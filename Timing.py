import difflib
from tkinter import Button, Frame,Label, Tk
from tkinter.constants import NORMAL, DISABLED
from time import perf_counter
from turtle import onclick
from Data import Data

class Timing:
    tic = None
    toc= None
    timelist = []
    entry=None
    text_to_be_typed = ""
    

    def __init__(self, main_frame, entry, text_to_be_typed):
        # Creating Frame for Buttons
        self.button_frame = Frame(main_frame, padx=15, pady=15)
        self.button_frame.grid(row=4, column =0) 

        #Creating Buttons
        self.start_button = Button( self.button_frame,  text="Start",  command= lambda: self.start())
        self.finish_button = Button(self.button_frame, text = 'Finish', command= lambda: self.on_click())
        self.pause_button = Button(self.button_frame, text = 'Pause', command= lambda: self.pause() )

        self.entry = entry
        self.text_to_be_typed = text_to_be_typed

    @staticmethod
    def sec_to_HMS(sec):
        #This function converts seconds into HH:MM:SS format
        HH = sec // 3600
        MM = sec % 3600 // 60
        SS = sec % 3600 % 60
        return f'{int(HH):02d}:{int(MM):02d}:{int(SS):02d}'


    def mistakes_list(self,alpha):
        #This function returns the list of words written incorrectly by the user.It takes the text entered by the user as an argument.
        res =[]
        for i in list(difflib.unified_diff(self.text_to_be_typed.split(),alpha.split())):
            if i[0]=='-':
                i = i.lstrip ('-')
                if i != '' and i != ' \n':          
                    res.append(i)
        return res


    def on_click(self):
    #This function displays a window with results shown when called and ends the counter
        self.entry.config(state=DISABLED)
        self.toc = perf_counter()
        results_window = Tk()
        results_window.resizable(0,0)
        results_window.attributes('-topmost',True)

        entered_text = self.entry.get("1.0","end")

        if self.mistakes_list(entered_text) == []:

            progress_frame = Frame(results_window)
            progress_frame.grid()

            res = self.toc-self.tic
            for i in self.timelist:
                res += i
                
            # Calculating WPM
            words_in_text=len(self.text_to_be_typed.split()) 

            time_in_minutes = res/60    

            WPMValue = words_in_text/time_in_minutes

            if WPMValue >= 80:
                title = Label(progress_frame, text="Well done! You have entered the text correclty and your typing speed is very good!", font=("Times New Roman",10,'bold') , fg = "green")  
            elif WPMValue<35:
                title = Label(progress_frame, text="You have entered your text correctly. Your typing speed is low. You need more practice. ", font=("Times New Roman",10,'bold') , fg = "red")
            else:
                title = Label(progress_frame, text="You have entered your text correctly. Your typing speed is ok", font=("Times New Roman",10,'bold') , fg = "orange")

            
            title.grid(padx=10, pady=10)

            
            timer = Label(progress_frame, text='Timer',font=("Times New Roman",12, 'bold'), pady=3)
            timer.grid(row=1)
        
            timerValue = Label(progress_frame, text = self.sec_to_HMS(res) , font=("Times New Roman",12), pady= 3)
            timerValue.grid(row=2, column=0)

            wpm = Label(progress_frame, text='WPM',font=("Times New Roman",12, 'bold'), pady =3)
            wpm.grid(row=3, column=0)


            wpm_value = Label(progress_frame, text = WPMValue, font=("Times New Roman",12), pady= 3)
            wpm_value.grid(row=4, column=0)

            

            self.pause()

        else:

            error_message = Label(results_window, text= 'Your text is not correctly entered. Close this window and correct your mistake(s).',font=("Times New Roman",12, 'bold'), pady =3)
            error_message.grid()

            self.mistakes_string ="\n"
            for i in self.mistakes_list(entered_text):
                self.mistakes_string = self.mistakes_string +i+'\n'

            mistakes = Label( results_window, text= "Problematic word(s) :" + self.mistakes_string, font=("Times New Roman",12, 'bold'), pady = 3 )
            mistakes.grid(row=1, column=0)

            accuracy= Label(results_window, text='Accuracy rate :',font=("Times New Roman",12, 'bold'), pady =3)
            accuracy.grid(row=3, column=0)
          
            value_of_accuracy = ((len(self.text_to_be_typed.split())-len(self.mistakes_list(entered_text)))/len(self.text_to_be_typed.split()))*100

           

            accuracy_value = Label(results_window, text = value_of_accuracy , font=("Times New Roman",12), pady= 3)
            accuracy_value.grid(row=4, column=0)

            # storing the mistakes of user in database

            query = """ SELECT mistakes
                    FROM Users 
                    WHERE email = ?;"""

            cursor= Data.database.execute(query,[Data.email_connected])

            mistakes_string= cursor.fetchone()[0]


            query = """UPDATE Users
                    SET mistakes = ?
                    WHERE email = ?;"""


            cursor= Data.database.execute(query, [mistakes_string+' '+' '.join(self.mistakes_list(entered_text)), Data.email_connected])
        

            data = cursor.execute('''SELECT * FROM users''')
            


            Data.database.commit()

            self.start()
       
        return None


    
    def start(self):
    # Creating start button function  
        self.pause_button.config(state=NORMAL)
        self.start_button.config(state=DISABLED)
        self.tic= perf_counter()
        self.entry.config(state=NORMAL)
        return None


    def pause(self):
    # Creating pause button function    
        self.pause_button['state']=DISABLED
        self.start_button.config(state=NORMAL)
        self.entry.config(state=DISABLED)
        end_of_time_period = perf_counter()
        time_period = end_of_time_period -self.tic
        self.timelist.append(time_period)
        return None
        

    def Buttons(self):  
        self.start_button.grid(row = 0, column= 0, padx= 10)  
        self.finish_button.grid(row=0, column = 1, padx=10)
        self.pause_button.grid(row = 0, column=2, padx=10)