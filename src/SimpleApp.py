from data import Dict

hex_Dict = Dict.dict

value_1 = input(str("Primeiro valor: ")).upper()
value_2 = input(str("Segundo valor: ")).upper()

if value_1 not in hex_Dict or value_2 not in hex_Dict:
    print("Valor inválido, tente entre: (1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)")
else:
    if value_1 == "1" or value_2 == "1":
        print(f"Resultado: {max(value_1,value_2)}")
    elif value_1 == "0" or value_2 == "0":
        print(f"Resultado: 0")        
    else:
        print(f"Resultado: {hex_Dict.get(value_1, {}).get(value_2, None)[0]}")
