# Inverter uma string
def inverterString(s):
    stringInvertida = ""
    
    for i in range(len(s) - 1, -1, -1):
        stringInvertida += s[i] 
    return stringInvertida

# Entrada
entrada = input("Digite uma string: ")

# Se não fornecer uma string
if entrada == "":
    entrada = "Exemplo de string"

resultado = inverter_string(entrada)
print(f"String invertida é {resultado}")
