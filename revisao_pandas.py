## Revisao Pandas - Parte 1
import pandas as pd

arquivo = "C:/Users/isabe/Documents/PROJETOS/revisaoAnalise/dados/myntra_dataset_ByScraping.csv"
df = pd.read_csv(arquivo)

# 1. Cinco primeiras e ultimas linhas do df
df.head(5)
df.tail(5)

# 2. Exibir numero de linhas e colunas
df.shape

# 3. Listar nomes colunas
df.columns

# 4. Mostrar os type das colunas 
df.dtypes

# 5. Info para olhar as informacoes gerais 
df.info()

# 6. marcas (brand_name) que temos 
df['brand_name'].unique()

# 7. Filtrar (produtos) > que 1.000 e < 3.000
filtro_preco = df[(df['price'] > 1000) & (df['price'] < 3000)]

# 8. df2 = brand_name, pants_description e price
df2 = df[['brand_name', 'pants_description', 'price']]

# 9. Filtrar os produtos da marca Roadster e criar um df_roadster
df_roadster = df[df['brand_name'] == 'Roadster']

# 10. verificar valores nulos em cada colunas
print(df.isnull().sum())

# 11. Top 10 produtos mais caros em ordem decrescente
top_10 = df.sort_values(by='price', ascending=False).head(10)

# 12. Preco medio
media = df['price'].mean()

# 13. Preco mediano
mediana = df['price'].median()

# 14. Desvio padrao 
dp = df['price'].std()

# 15. valores max e min do desconto (discount_percent)
valor_max = df['discount_percent'].min()
valor_min = df['discount_percent'].max()

# 16. Quantos produtos estao acima e abaixo da media (pride)
abaixo_media = df[df['price'] < media].shape[0]
acima_media =  df[df['price'] > media].shape[0]

# 17. Adicionar nova coluna desconto
df['preco_desconto'] = df['MRP'] * (1 - df['discount_percent'])

# 18. Remover todos os produtos com ratings menores que 2.0
df = df[df['ratings'] >= 2.0]

# 19. Excluir coluna pants_description
df.drop(columns=['pants_description'], axis=1)

# 20. Agrupar por marca e calcular (price) medio
preco_medio = df.groupby('brand_name')['price'].mean()