def HexToInt(hex): 
    if "0" <= hex <= "9":
        return (ord(hex) - ord("0"))
    elif "A" <= hex <= "F":
        return ((ord(hex) - ord("A")) + (ord("K") - ord("A")))
    else:
        raise ValueError("Valor Inválido")

def IntToHex(num):
    if (ord("0") - ord("0")) <= num <= (ord("9") - ord("0")):
        return chr(ord("0") + num)
    else:
        return chr((ord("A") + num) - (ord("K") - ord("A")))

# def MultHex(value1,value2):
#     if not (value1 and value2) or not all(c in "0123456789ABCDEF" for c in value1+value2):
#         raise ValueError("Valor Inválido")
    
#     result = []

#     # result = [(ord("0") - ord("0"))] * (len(value1)+len(value2))
#     for i,char1 in enumerate(value1):
#         for j,char2 in enumerate(value2):
#             int1 = HexToInt(char1)
#             int2 = HexToInt(char2)

#             position = i + j

#             result[position] = [int1,int2]

#     print(result)

#     # for i,char1 in enumerate(reversed(value1)):
#     #     for j,char2 in enumerate(reversed(value2)):
#     #         int1= HexToInt(char1)
#     #         int2= HexToInt(char2)

#     #         product = int1 * int2
#     #         position = i + j

#     #         result[position] += product

#     #         result[position + (ord("1") - ord("0"))] += result[position] // (ord("Q") - ord("A"))

#     #         result[position] %= (ord("Q") - ord("A"))

#     # result = ''.join(IntToHex(x) for x in reversed(result)).lstrip('0')
#     # return result
    
# MultHex("25".upper(),"5".upper())


# valor1 = [1,2,3]
# valor2 = [3,2,1]

# listaValores = [["0","8","E","3","1"],["3","13",'2',"2","F"]]

# # ListaLen = [4,5]

# listaLen = list(len(lista) for lista in listaValores) ## Forma uma tupla com o tamanho de cada valor
# print(f"Tamanho das Listas: {listaLen}")

# if all(x == listaLen[0] for x in listaLen): ## Verifica se todos os valores sao do mesmo tamanho
#     a = listaValores[0]
#     b = listaValores[1]

#     print(a)
#     print(b)
#     print()

#     resultado = [0] * ((listaLen[0]) + 1)
#     print(resultado)
    
#     for i,(x,y) in enumerate(reversed(list(zip(a,b)))):
#         x = HexToInt(x)
#         y = HexToInt(y)

#         print(f"Index: {i}, Valores: {x} + {y}")

#         i += 1
#         soma = x + y
#         counter = 0

#         if soma >= 16:
#             soma -= 16
#             counter += 1

#         resultado[-(i+1)] += soma

#         if (i + 1) < len(resultado):
#             resultado[-(i+2)] += counter

#         resultado = ''.join(IntToHex(x) for x in reversed(resultado)).lstrip('0')
        

#         print(f"Counter: {counter}, Resultado: {resultado}")
#         print()

# else:
#     menorValor = min(listaValores, key=len)
#     maiorValor = max(listaValores, key=len)

#     while len(menorValor) < len(maiorValor): 
#         menorValor.insert(0,0)

#     print(f"Maior Valor: {maiorValor}")
#     print(f"Menor Valor: {menorValor}")
#     print()

#     resultado = [0] * (len(maiorValor) + 1)
#     print(f"Lista de 0: {resultado}")
#     print()
    
#     for i,(x,y) in enumerate(reversed(list(zip(maiorValor,menorValor)))):
#         print(f"Index: {i}, Valores: {x} + {y}")

#         i += 1
#         soma = x + y
#         counter = 0

#         if soma >= 16:
#             soma -= 16
#             counter += 1

#         resultado[-(i+1)] += soma

#         if (i + 1) < len(resultado):
#             resultado[-(i+2)] += counter

#         print(f"Counter: {counter}, Resultado: {resultado}")
#         print()


# def SumHex(value1,value2):
#     if not (value1 and value2) or not all(c in "0123456789ABCDEF" for c in value1+value2):
#         raise ValueError("Valor Inválido")
    
#     values = [value1,value2]

#     result = [0] * (len(value1))

# value1 = "03423"
# value2 = "0FA21"

# result = (len(value1)+1) * [0]

# print(f"Valor1: [{value1}]")
# print(f"Valor2: [{value2}]")
# print()

# for i,(x,y) in enumerate(reversed(list(zip(value1,value2)))):
#         x = HexToInt(x)
#         y = HexToInt(y)
#         # print(f"Index: {i}, Valores: {x} + {y}")

#         sum = x + y
#         counter = 0

#         if sum >= 16:
#             sum -= 16
#             counter += 1

#         result[(i)] += sum

#         if (i + 1) < len(result):
#             result[(i+1)] += counter
       
# result = ''.join(IntToHex(x) for x in reversed(result)).lstrip("0")

def SumHex(a,b):
    value1 = a.upper()
    value2 = b.upper()

    ListaValores = [[value1],[value2]]

    if not (value1 and value2) or not all(c in "0123456789ABCDEF" for c in value1+value2):
        raise ValueError("Valor Inválido")
    
    ListaLen = [[len(value1)], [len(value2)]]

    if all(x == ListaLen[0] for x in ListaLen):

        result = (len(value1)+1) * [0]

        for i,(x,y) in enumerate(reversed(list(zip(value1,value2)))):
            x = HexToInt(x)
            y = HexToInt(y)
            # print(f"Index: {i}, Valores: {x} + {y}")

            sum = x + y
            counter = 0

            if sum >= 16:
                sum -= 16
                counter += 1

            result[(i)] += sum

            if (i + 1) < len(result):
                result[(i+1)] += counter
        
        result = ''.join(IntToHex(x) for x in reversed(result)).lstrip("0")

        return result
    
    else:
        print()



valor1 = input("Insira o primeiro valor: ")
valor2 = input("Insira o segundo valor: ")

print(SumHex(valor1,valor2))