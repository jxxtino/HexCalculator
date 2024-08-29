from .Controllers.Controller import Controllers_

class Addition():
    def SumHex(self,value1,value2):
        value1 = value1.upper()
        value2 = value2.upper()

        if not(value1 and value2):
            raise ValueError("Valor Inválido")

        Values = [value1,value2]
        ValuesLen = [len(value1),len(value2)]

        if not all(x == ValuesLen[0] for x in ValuesLen):
            value1 = max(Values, key=len)
            value2 = min(Values, key=len)

            while len(value2) < len(value1):
                value2 = "0" + value2

            Values = [value1,value2]

        result = [0] * (len(Values[0]) + 1)

        for i,(x,y) in enumerate(reversed(list(zip(value1,value2)))):
            x = Controllers_.HexToInt(x)
            y = Controllers_.HexToInt(y)

            sum = x + y
            counter = 0

            result[(i)] += sum

            if result[(i)] >= 16:
                result[(i)] -= 16
                counter += 1

            if (i + 1) < len(result):
                result[(i+1)] += counter

        result = ''.join(Controllers_.IntToHex(x) for x in reversed(result)).lstrip("0")
        return result
    
Addition_ = Addition()