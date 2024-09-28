faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calcular o percentual
def calcularPercentuais(faturamento):
    totalFaturamento = sum(faturamento.values())
    percentuais = {}
    
    for estado, valor in faturamento.items():
        percentuais[estado] = (valor / totalFaturamento) * 100
    
    return percentuais

def imprimirPercentuais(percentuais):
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

# Chamadando as funções
percentuais = calcularPercentuais(faturamento)
imprimirPercentuais(percentuais)
