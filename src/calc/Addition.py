# def HexToInt(hex): 
#     if "0" <= hex <= "9":
#         return (ord(hex) - ord("0"))
#     elif "A" <= hex <= "F":
#         return ((ord(hex) - ord("A")) + (ord("K") - ord("A")))
#     else:
#         raise ValueError("Valor Inválido")

# def IntToHex(num):
#     if (ord("0") - ord("0")) <= num <= (ord("9") - ord("0")):
#         return chr(ord("0") + num)
#     else:
#         return chr((ord("A") + num) - (ord("K") - ord("A")))

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


valor1 = [1,2,3]
valor2 = [3,2,1]

listaValores = [[8,9,3,1],[3,5,2,2,5]]

listaLen = list(len(lista) for lista in listaValores) ## Forma uma tupla com o tamanho de cada valor


if all(x == listaLen[0] for x in listaLen): ## Verifica se todos os valores sao do mesmo tamanho
    print("==")
else:
    menorValor = min(listaValores, key=len)
    maiorValor = max(listaValores, key=len)

    while len(menorValor) < len(maiorValor):
        menorValor.insert(0,0)

    print(maiorValor)
    print(menorValor)
    print()

    resultado = [0] * (len(maiorValor) + 1)
    
    for i,(x,y) in enumerate(reversed(list(zip(maiorValor,menorValor)))):
        print(f"Index: {i}, Valores: {x} + {y}")

        i += 1
        soma = x + y
        counter = 0

        if soma >= 16:
            soma -= 16
            counter += 1

        resultado[-(i+1)] += soma

        if (i + 1) < len(resultado):
            resultado[-(i+2)] += counter

        print(f"Counter: {counter}, Resultado: {resultado}")
        print()


