from calc.Addition import Addition_
from calc.Multiplication import Multiplication_

class Calculator():

    def OperationHandler(self,a,b,c):
        value1 = a
        value2 = b
        operation = c
        
        while operation not in ["+","*"]:
            operation = input("Operação inválida. Tente novamente (+ ou *): ")

        if operation == "+":
            result = Addition_.SumHex(value1,value2)
        elif operation == "*":
            result = Multiplication_.MultHex(value1,value2)

        print(f"{value1} {operation} {value2} = {result}")

    def __init__(self):
        a = input("Primeiro valor: ")
        b = input("Segundo valor: ")
        c = input("Operação (+ ou *): ")

        self.OperationHandler(a,b,c)

if __name__ == "__main__":
    Calculator_ = Calculator()

