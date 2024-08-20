def HexToInt(char):
    if "0" <= char <= "9":
        return ( ord(char) - ord("0") )
    elif "A" <= char <= "F":
        return ( ord(char) - ord("A") + 10 )
    else:
        raise ValueError("Valores Inválidos")
    
def IntToHex(num):
    if 0 <= num <= 9:
        return chr( ord("0") + num )
    else:
        return chr( ord("A") + num - 10)

def MultiplyHex(value1,value2):
    value1 = value1.upper()
    value2 = value2.upper()
    
    if not (value1 and value2) or not all( char in "0123456789ABCDEF" for char in value1+value2 ):
        raise ValueError("Valores Inválidos")
    
    result = [0] * (len(value1) + len(value2))

    for i,char1 in enumerate(reversed(value1)):
        for j,char2 in enumerate(reversed(value2)):
            int1 = HexToInt(char1)
            int2 = HexToInt(char2)
    
            product = int1 * int2
            position = i + j

            result[position] += product

            result[position + 1] += result[position] // 16
            result[position] %= 16

    result = ''.join(IntToHex(x) for x in reversed(result))
    return result

a = str(input("Primeiro valor: ")).upper()
b = str(input("Segundo valor: ")).upper()

try: 
    ab = MultiplyHex(a,b)
    print(f"Multiplicando {a} e {b} temos: '{ab}' ")

except ValueError as error:
    print(error)