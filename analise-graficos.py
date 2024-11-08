import pandas as pd
import matplotlib.pyplot as plt

# insira os dados corretamente para a analise
## [dados em questão são somente para simulacao]
data = {'Categoria': ['Eletrônicos', 'Moda', 'Casa e Decoração', 'Livros', 'Esportes'],
        'Vendas': [520, 340, 210, 175, 115]}
df = pd.DataFrame(data)
plt.bar(df['Categoria'], df['Vendas'], color='blue')
plt.xlabel('Categoria de Produto')
plt.ylabel('Vendas')
plt.title('Vendas por Categoria')
plt.show()

df['Data'] = pd.date_range(start='1/1/2024', periods=5, freq='M')
plt.plot(df['Data'], df['Vendas'])
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Vendas Mensais')
plt.show()

df['Data'] = pd.date_range(start='1/1/2024', periods=5, freq='M')
plt.plot(df['Data'], df['Vendas'])
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Vendas Mensais')
plt.show()
