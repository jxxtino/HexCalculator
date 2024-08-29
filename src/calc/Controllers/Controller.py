class Controllers():

    def HexToInt(self,hex):
        if "0" <= hex <= "9":
            return (ord(hex) - ord("0"))
        elif "A" <= hex <= "F":
            return ((ord(hex) - ord("A")) + (ord("K") - ord("A")))
        else:
            raise ValueError("Valor Inválido")
        
    def IntToHex(self,num):
        if (ord("0") - ord("0")) <= num <= (ord("9") - ord("0")):
            return chr(ord("0") + num)
        else:
            return chr((ord("A") + num) - (ord("K") - ord("A")))
    
Controllers_ = Controllers()