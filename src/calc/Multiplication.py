from .Controllers.Controller import Controllers_

class Multiplication():

    def MultHex(self,value1,value2):
        value1 = value1.upper()
        value2 = value2.upper()

        if not (value1 and value2) or not all(c in "0123456789ABCDEF" for c in value1+value2):
            raise ValueError("Valor Inválido")
        
        result = [(ord("0") - ord("0"))] * (len(value1)+len(value2))

        for i,char1 in enumerate(reversed(value1)):
            for j,char2 in enumerate(reversed(value2)):
                int1= Controllers_.HexToInt(char1)
                int2= Controllers_.HexToInt(char2)

                product = int1 * int2
                position = i + j

                result[position] += product

                result[position + (ord("1") - ord("0"))] += result[position] // (ord("Q") - ord("A"))

                result[position] %= (ord("Q") - ord("A"))

        result = ''.join(Controllers_.IntToHex(x) for x in reversed(result)).lstrip('0')
        return result
    
Multiplication_ = Multiplication()