#################################################################
# File name:Carlos-Final-Exame-SDUIS.py                         #
# APP Name = Ride a Mountain                                    #
# Author: Carlos Lucio Junior                                   #
# Date:06-22-2021                                               #
# Classes:  ITS 220: Programming Languages & Concepts           #
# Instructor: Matthew Loschiavo                                 #
# This is a Final Exame                                         #
# Create a game to teach kindergartners how to sum              #
# You can find all the files used in this code at               #
# https://github.com/J4rn3s/FinalExame                          #
#################################################################
# Importing session from and excel spreadsheet
import pandas as pd

from tkinter import *
from tkinter import messagebox

#Variables definitions for questions. Defining values to determine the results and to bring the correct information from the table.
def result():

    valid = True

    while valid == True:
        try:
            result= int(gear.get())+int(goofy.get())+int(practice.get())+int(groomer.get())
            valid = False
        except ValueError:
            messagebox.showwarning('Alert','Looks like you are missing something. Make sure you answered all the questions') # Validation if it is not a letter
            break

        name = str(depot.get())
        mtrecommend_df = pd.read_excel(r"C:\Finalexame\finaldata.xlsx", engine='openpyxl')

        if result == 0:
            messagebox.showinfo('Level Result', "Noob")
            Output.insert(END, "No problem, "+name+"\nEveryone has to start from somewhere. The recommended mountain for you is Snow Valey. ")
            a = (mtrecommend_df.loc[mtrecommend_df['score'] == result, ['description','site']])
            b = str(a.to_string(index=False, header=False))
            Output.insert(END, b)

        elif result == 10:
            messagebox.showinfo('Level Result', "Beginner")
            Output.insert(END, "That is great "+name+"\n,looks like you know something. The recommended Mountain for you is  Snow Valley. ")
            c = (mtrecommend_df.loc[mtrecommend_df['score'] == result, ['description', 'site']])
            d = str(c.to_string(index=False, header=False))
            Output.insert(END, d)

        elif result == 20:
            messagebox.showinfo('Level Result', "Intermediate")
            Output.insert(END, "Nice "+name+"\n, looks like you have some skills. The recommended Mountain for you is Mountain High. ")
            e = (mtrecommend_df.loc[mtrecommend_df['score'] == result, ['description', 'site']])
            f = str(e.to_string(index=False, header=False))
            Output.insert(END, f)

        elif result == 30:
            messagebox.showinfo('Level Result', "Advanced")
            Output.insert(END, "Sick "+name+".\n We can tell that you at least ride 4 fun. The recommended Mountain for you is Big Bear / Snow Summit. ")
            g = (mtrecommend_df.loc[mtrecommend_df['score'] == result, ['description', 'site']])
            h = str(g.to_string(index=False, header=False))
            Output.insert(END, h)

        elif result == 40:
            messagebox.showinfo('Level Result', "Expert")
            Output.insert(END,"Dope "+name+"!\n You are probably preparing yourself for the X-Games! The recommended Mountain for you is Mammoth! ")
            i = (mtrecommend_df.loc[mtrecommend_df['score'] == result, ['description', 'site']])
            j = str(i.to_string(index=False, header=False))
            Output.insert(END, j)

#Exit Application Button
def ExitApplication():
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',icon='warning')

    if MsgBox == 'yes':
        app.destroy()
    else:
       messagebox.showinfo('Return', 'You will now return to the application screen')

#def sos(): #Here I tried to implement a save button for the results. It did not work.#
   ## messagebox.showinfo('SOS', 'CALL 911')

app = Tk()
app.title('Ride a Mountain')
Label(app, text = "Enter your name",bg="light blue").pack()
depot = Entry(app)
depot.pack()

#Question 1
Label(app, text = "Do you need to rent your Snowboard gear?").pack()
gear = StringVar()
gear.set(None)
Radiobutton(app, variable = gear, text = "Yes", value = 0).pack()
Radiobutton(app, variable = gear, text = "No", value = 10).pack()

#Question 2
Label(app, text = "Do you know what Regular and Goofy means?").pack()
goofy = StringVar()
goofy.set(None)
Radiobutton(app, variable = goofy, text = "Yes", value = 10).pack()
Radiobutton(app, variable = goofy, text = "No", value = 0).pack()

#Question 3
Label(app, text = "Have you ever practice Skateboard or Surf before?").pack()
practice = StringVar()
practice.set(None)
Radiobutton(app, variable = practice, text = "Yes", value = 10).pack()
Radiobutton(app, variable = practice, text = "No", value = 0).pack()

#Question4
Label(app, text = "Do you know what is a groomer?").pack()
groomer = StringVar()
groomer.set(None)
Radiobutton(app, variable = groomer, text = "Yes", value = 10).pack()
Radiobutton(app, variable = groomer, text = "No", value = 0).pack()

Output = Text(app, height=15,width=68,bg="light gray")
Output.pack()

Button(app, text = "Results", command = result, bg="blue", fg="white").pack()
#Exit Application Window
Button(app, text='Exit Application', command=ExitApplication, bg='brown', fg='white').pack()
#Button(app, text = "SOS", command = sos).pack() #Part of the save button#
app.mainloop()

