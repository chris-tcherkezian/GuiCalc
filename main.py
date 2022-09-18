from tkinter import *

#layout
# _____________________
#|                     |
#|      Text Box       |
#|_____________________|
#|                     |
#| 7     8    9    +   |
#| 4     5    6    -   |
#| 1     2    3    *   |
#| AC    0    =    /   |
#|_____________________|

#-----------FUNCTIONS FOR CALCULATOR-----------#

#Clear the contents in text box
def clearcalc():

#Calculator expression evaluation
def eval():

#Update contents of text box on pressing buttons
def onPress():


#--------------MAIN DRIVER CODE----------------#

if __name__=="__main__":
#create gui window itself using tkinter
    gui = Tk()

    #Title of gui
    gui.title("CS4800 Calculator")

    #gui window size
    gui.geometry("275x250")

    #text box declaration
    #Tkinter Entry widget accepts single-line text string from user
    textbox = Entry(gui)

    #grid size declaration
    #grid organizes widgets in the table
    #ipadx pads the horizontal widgets borders
    textbox.grid(columnspan=4, ipadx=70)

    #buttons & button locations (using grid)
    button1 = Button(gui, text=' 1 ', command=lambda: )
    button1.grid(row=4, column=0)

    button2 = Button(gui, text=' 2 ', command=lambda: )
    button2.grid(row=4, column=1)

    button3 = Button(gui, text=' 3 ', command=lambda: )
    button3.grid(row=4, column=2)

    button4 = Button(gui, text=' 4 ', command=lambda: )
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', command=lambda: )
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', command=lambda: )
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', command=lambda: )
    button7.grid(row=2, column=0)

    button8 = Button(gui, text=' 8 ', command=lambda: )
    button8.grid(row=2, column=1)

    button9 = Button(gui, text=' 9 ', command=lambda: )
    button9.grid(row=2, column=2)

    button0 = Button(gui, text=' 0 ', command=lambda: )
    button0.grid(row=5, column=1)

    plus = Button(gui, text=' + ', command=lambda: )
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', command=lambda: )
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', command=lambda: )
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', command=lambda: )
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', command= onPress)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='AC', command = clearcalc)
    clear.grid(row=5, column='0')

    #gui start (starts the gui application)
    gui.mainloop()