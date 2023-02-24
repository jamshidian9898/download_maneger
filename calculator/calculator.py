from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x422+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold',28), textvariable=self.equation).place(y=0, x=0)
        self.buttons()

    def show(self, Value):
        self.entry_value += str(Value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

    def buttons(self):
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.show(str('('))).place(x=0,y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda:self.show(str(')'))).place(x=90,y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda:self.show(str('%'))).place(x=180,y=50)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda:self.show(str('/'))).place(x=270,y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda:self.show(str('1'))).place(x=0,y=125)
        Button(width=11, height=4, text=2, relief='flat', bg='white', command=lambda:self.show(str(2))).place(x=90,y=125)
        Button(width=11, height=4, text=3, relief='flat', bg='white', command=lambda:self.show(str(3))).place(x=180,y=125)
        Button(width=11, height=4, text='*', relief='flat', bg='white', command=lambda:self.show(str('*'))).place(x=270,y=125)
        Button(width=11, height=4, text=4, relief='flat', bg='white', command=lambda:self.show(str(4))).place(x=0,y=200)
        Button(width=11, height=4, text=5, relief='flat', bg='white', command=lambda:self.show(str(5))).place(x=90,y=200)
        Button(width=11, height=4, text=6, relief='flat', bg='white', command=lambda:self.show(str(6))).place(x=180,y=200)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda:self.show(str('-'))).place(x=270,y=200)
        Button(width=11, height=4, text=7, relief='flat', bg='white', command=lambda:self.show(str(7))).place(x=0,y=275)
        Button(width=11, height=4, text=8, relief='flat', bg='white', command=lambda:self.show(str(8))).place(x=90,y=275)
        Button(width=11, height=4, text=9, relief='flat', bg='white', command=lambda:self.show(str(9))).place(x=180,y=275)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda:self.show(str('+'))).place(x=270,y=275)
        Button(width=11, height=4, text='C', relief='flat', bg='red', command=self.clear).place(x=0,y=350)
        Button(width=11, height=4, text=0, relief='flat', bg='white', command=lambda:self.show(str(0))).place(x=90,y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda:self.show(str('.'))).place(x=180,y=350)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270,y=350)

        # didnt work, problem = for all buttons '=' char sets in command.
        # btn_list = [
        #     ['(',')','%','/'],
        #     [1,2,3,'x'],
        #     [4,5,6,'-'],
        #     [7,8,9,'+'],
        #     ['c',0,'.','=']
        # ]

        # x= 0
        # y= 50
        # for row in btn_list:
        #     for btn in row:
        #         print(btn,x,y)
        #         Button(width=11, height=4, text=btn, relief='flat', bg='white', command=lambda:self.show(str(btn))).place(x=x,y=y)
        #         print(btn)
        #         x += 90
        #     y += 75
        #     x = 0

root = Tk()
calculator = Calculator(root)
root.mainloop()