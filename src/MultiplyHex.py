def HexToInt(hex): 
    if "0" <= hex <= "9":
        return (ord(hex) - ord("0"))
    elif "A" <= hex <= "F":
        return ((ord(hex) - ord("A")) + (ord("K") - ord("A")))
    else:
        raise ValueError("Valor Inválido")

def IntToHex(num):
    if (ord("0")-ord("0")) <= num <= (ord("9")-ord("0")):
        return chr(ord("0") + num)
    else:
        return chr((ord("A") + num) - (ord("K") - ord("A")))

def MultHex(value1,value2):
    value1 = value1.upper()
    value2 = value2.upper()

    if not (value1 and value2) or not all(c in "0123456789ABCDEF" for c in value1+value2):
        raise ValueError("Valor Inválido")
    
    result = [(ord("0")-ord("0"))] * (len(value1)+len(value2))

    for i,char1 in enumerate(reversed(value1)):
        for j,char2 in enumerate(reversed(value2)):
            int1= HexToInt(char1)
            int2= HexToInt(char2)

            product = int1 * int2
            position = i + j

            result[position] += product

            result[position + (ord("1")-ord("0"))] += result[position] // (ord("Q") - ord("A"))

            result[position] %= (ord("Q") - ord("A"))

    result = ''.join(IntToHex(x) for x in reversed(result)).lstrip('0')
    return result

a = str(input("Valor 1: ")).upper()
b = str(input("Valor 2: ")).upper()

try:
    ab = MultHex(a,b)
    print(f"A multiplicação entre {a} e {b} é: {ab}")
except ValueError as error:
    print(error)