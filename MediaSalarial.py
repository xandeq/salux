import pandas as pd

dados = {
    'identificador': [1, 2, 3, 4, 5],
    'pessoa': ['Alice', 'Bob', 'Carlos', 'Daniel', 'Eva'],
    'anos': [25, 30, 35, 40, 45],
    'renda': [5000, 7000, 8000, 10000, 12000]
}

tabela = pd.DataFrame(dados)

def calcular_media_renda(tabela):
    return tabela[tabela['anos'] > 30]['renda'].mean()

resultado = calcular_media_renda(tabela)
print(resultado)
