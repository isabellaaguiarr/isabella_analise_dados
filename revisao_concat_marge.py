## Revisao Concat e Merge - Parte 2 
import pandas as pd

arquivo = "C:/Users/isabe/Documents/PROJETOS/revisaoAnalise/dados/myntra_dataset_ByScraping.csv"
df = pd.read_csv(arquivo)

# 1. 
dados_novos_produtos = {
    "brand_name": ["Myntra Basics", "Denim Pro", "Urban Style"],
    "pants_description": [
        "Men Slim Fit Blue Jeans",
        "Men Regular Fit Jeans",
        "Men Tapered Fit Jeans"
    ],
    "price": [1299, 1599, 1899],
    "MRP": [1999, 2499, 2899],
    "discount_percent": [0.35, 0.40, 0.34],
    "ratings": [4.1, 3.8, 4.3],
    "number_of_ratings": [23, 12, 47]
}

df_novos_produtos = pd.DataFrame(dados_novos_produtos)
df = pd.concat([df, df_novos_produtos])

# 2. 
dados_promocoes = {
    "brand_name": ["Test Brand A", "Test Brand B", "Test Brand C"],
    "pants_description": [
        "Men Slim Fit Black Jeans",
        "Men Regular Fit Grey Jeans",
        "Men Loose Fit White Jeans"
    ],
    "discount_percent": [0.50, 0.60, 0.45]
}
df_promocoes = pd.DataFrame(dados_promocoes)

concat_linhas = pd.concat([df_promocoes, df], axis=0)
# concat_colunas = pd.concat([df_promocoes, df], axis=1)

# 3. 
dados_marcas_info = {
    "brand_name": ["Roadster", "WROGN", "Flying Machine", "Urban Style"],
    "country": ["India", "India", "USA", "Brazil"],
    "year_founded": [2012, 2014, 1980, 2018]
}
df_marcas_info = pd.DataFrame(dados_marcas_info)
df_merge_marcas = pd.merge(df, df_marcas_info, on="brand_name", how="inner")
# pd.merge(df, df_marcas_info, on="brand_name", how="inner") # Poderia ser so assim, sem definir 

# 4. 
dados_categorias = {
    "pants_description": [
        "Men Slim Fit Jeans",
        "Men Regular Fit Jeans",
        "Men Loose Fit Cotton Jeans",
        "Men Tapered Fit Jeans"
    ],
    "category": ["Slim", "Regular", "Loose", "Tapered"]
}
df_categorias = pd.DataFrame(dados_categorias)
df_merge_categorias = pd.merge(df, df_categorias, on="pants_description", how="inner")

# 5. 
dados_ratings_extra = {
    "brand_name": ["Roadster", "WROGN", "Urban Style"],
    "avg_new_rating": [4.0, 4.3, 4.1]
}
df_ratings_extra = pd.DataFrame(dados_ratings_extra)
df_merge_ratings = pd.merge(df, df_ratings_extra, on="brand_name", how="left")