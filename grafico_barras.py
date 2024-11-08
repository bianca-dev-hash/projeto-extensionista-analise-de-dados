import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Categoria': ['Eletrônicos', 'Moda', 'Casa e Decoração', 'Livros', 'Esportes'],
    'Vendas': [524, 373, 237, 137, 137]
}
df = pd.DataFrame(data)


plt.figure(figsize=(8, 5))
plt.bar(df['Categoria'], df['Vendas'], color='skyblue')
plt.xlabel('Categoria de Produto')
plt.ylabel('Vendas (em unidades)')
plt.title('Vendas por Categoria de Produto')
plt.show()