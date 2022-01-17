from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main,self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 20, "bold"), bg = "#fff", foreground = "#000")
        self.lbl.place(x=11, y=50)
# Кнопки
        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "x^2"
            ]
        x = 10
        y = 140
        for bt in btns:
            com = lambda x = bt: self.logicalc(x)
            Button(text=bt,bg="#F4F",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def calc(self,formula):
        k=formula.find("^")
        if k==-1:
           return str(eval(formula))
        else:
           a=formula[0:k]
           b=formula[k+1:]
           return str(eval("math.pow("+a+","+b+")"))

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "x^2":
            self.formula = str((eval(self.formula))**2)  #eval возврат целого значения после вычисления
        elif operation == "=":
            self.formula = self.calc(self.formula)
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

if __name__ =='__main__':
    root = Tk()
    root["bg"] = "#FFF"
    root.geometry("500x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()