
from tkinter import *
import tkinter
from CalculatorLogic import CalculatorLogic


def captureText(input):
    inputText.insert(END, input)


def clearInput():
    inputText.delete(0, END)


def compute():
    calculator = CalculatorLogic()
    curExpression = inputText.get()
    answer = calculator.postFixEval(calculator.infixToPostFix(curExpression))
    # histBoxVal = (curExpression, "\t\t", answer)
    historyBox.insert(END, f"{curExpression}     =     {answer}")
    inputText.delete(0, END)


root = tkinter.Tk()
root.title("CALCULATOR")
root.option_add('*Font', 'Times 19')
root.geometry("500x500")


row6 = tkinter.Frame(root)
historyBox = tkinter.Listbox(row6, height=5, bg="white",
                             activestyle='dotbox',
                             fg="black")
scrollbar = tkinter.Scrollbar(row6)
scrollbar.pack(side=RIGHT, fill=BOTH)
scrollbar.config(command=historyBox.yview)
historyBox.config(yscrollcommand=scrollbar.set)
historyBox.pack(fill="both", expand=True, side="left")
row6.pack(fill="both", expand=True)

row5 = tkinter.Frame(root)
inputText = tkinter.Entry(row5)
inputText.pack(fill="both", expand=True, side="left")
row5.pack(fill="both", expand=True)

row4 = tkinter.Frame(root)
btnCancel = tkinter.Button(row4, text="C", command=clearInput)
btnCancel.pack(fill="both", expand=True, side="left")
btnBOpen = tkinter.Button(row4, text=" (", command=lambda: captureText("("))
btnBOpen.pack(fill="both", expand=True, side="left")
btnBClose = tkinter.Button(row4, text=")", command=lambda: captureText(")"))
btnBClose.pack(fill="both", expand=True, side="left")
btnDivide = tkinter.Button(row4, text="÷", command=lambda: captureText("/"))
btnDivide.pack(fill="both", expand=True, side="left")
row4.pack(fill="both", expand=True)

row3 = tkinter.Frame(root)
btn7 = tkinter.Button(row3, text="7", command=lambda: captureText(7))
btn7.pack(fill="both", expand=True, side="left")
btn8 = tkinter.Button(row3, text="8", command=lambda: captureText(8))
btn8.pack(fill="both", expand=True, side="left")
btn9 = tkinter.Button(row3, text="9", command=lambda: captureText(9))
btn9.pack(fill="both", expand=True, side="left")
btnMultiply = tkinter.Button(row3, text="X", command=lambda: captureText("*"))
btnMultiply.pack(fill="both", expand=True, side="left")
row3.pack(fill="both", expand=True)

row2 = tkinter.Frame(root)
btn4 = tkinter.Button(row2, text="4", command=lambda: captureText(4))
btn4.pack(fill="both", expand=True, side="left")
btn5 = tkinter.Button(row2, text="5", command=lambda: captureText(5))
btn5.pack(fill="both", expand=True, side="left")
btn6 = tkinter.Button(row2, text="6", command=lambda: captureText(6))
btn6.pack(fill="both", expand=True, side="left")
btnMinus = tkinter.Button(row2, text=" -", command=lambda: captureText("-"))
btnMinus.pack(fill="both", expand=True, side="left")
row2.pack(fill="both", expand=True)

row1 = tkinter.Frame(root)
btn1 = tkinter.Button(row1, text="1", command=lambda: captureText(1))
btn1.pack(fill="both", expand=True, side="left")
btn2 = tkinter.Button(row1, text="2", command=lambda: captureText(2))
btn2.pack(fill="both", expand=True, side="left")
btn3 = tkinter.Button(row1, text="3", command=lambda: captureText(3))
btn3.pack(fill="both", expand=True, side="left")
btnPlus = tkinter.Button(row1, text="+", command=lambda: captureText("+"))
btnPlus.pack(fill="both", expand=True, side="left")
row1.pack(fill="both", expand=True)


row0 = tkinter.Frame(root)
btn0 = tkinter.Button(row0, text="0", command=lambda: captureText(0))
btn0.pack(fill="both", expand=True, side="left")
btnDecimal = tkinter.Button(row0, text=" .", command=lambda: captureText("."))
btnDecimal.pack(fill="both", expand=True, side="left")
btnEqual = tkinter.Button(row0, text="=", width=6, command=compute)
btnEqual.pack(fill="both", expand=True, side="left")
row0.pack(fill="both", expand=True)


root.mainloop()
