from calc.Addition import Addition_
from calc.Multiplication import Multiplication_

class Calculator():

    def OperationHandler(self,a,b,c):
        value1 = a
        value2 = b
        operation = c
        
        if operation == "+":
            result = Addition_.SumHex(value1,value2)
        elif operation == "*":
            result = Multiplication_.MultHex(value1,value2)

        print(result)

    def __init__(self):
        a = input("Primeiro valor: ")
        b = input("Segundo valor: ")
        c = input("Operação: ")

        self.OperationHandler(a,b,c)

if __name__ == "__main__":
    Calculator_ = Calculator()

