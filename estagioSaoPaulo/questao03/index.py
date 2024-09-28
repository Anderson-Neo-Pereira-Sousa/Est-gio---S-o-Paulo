import json

# Calcula o faturamento
def calcularFaturamento(faturamento):
    with open('arquivo.json', 'r') as file: # colocar direito o nome do arquivo caso for tire do repositõrio 
        data = json.load(file)
        
    faturamentoDiario = data['faturamento']
    
    # Filtra os dia sem faturamento
    valores = [item['valor'] for item in faturamentoDiario if item['valor'] > 0]
    
    if not valores:
        print("Não há dias com faturamento. POde ser um erro na lista.")
        return

    menorFaturamento = min(valores)
    maiorFaturamento = max(valores)
    mediaMensal = sum(valores) / len(valores)

    # Dias com faturamento acima da média
    diasAcimaMedia = sum(1 for valor in valores if valor > mediaMensal)

    print(f"Menor faturamento: R$ {menorFaturamento:.2f}")
    print(f"Maior faturamento: R$ {maiorFaturamento:.2f}")
    print(f"Número de dias acima da média: {diasAcimaMedia}")

# Chamada da função
calcularFaturamento('arquivo.json')
