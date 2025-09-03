import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import DataFrame, StrVector, FloatVector

# Ler arquivo 
arquivo = "C:/Users/isabe/Documents/PROJETOS/analise_python_r/data/filmes.xlsx"
df = pd.read_excel(arquivo)

# Limpando df 
df.columns = df.columns.str.strip()
df = df.dropna(subset=['Genero', 'Bilheteria'])

print("Dados limpos do Excel:")
print(df)
print("\n")

# Convertendo os dados para R
dados_r = DataFrame({
    'Genero': StrVector(df['Genero'].astype(str)),
    'Bilheteria': FloatVector(df['Bilheteria'].astype(float))
})

# Calculando média da bilheteria por genero com R
aggregate = ro.r['aggregate']
res = aggregate(ro.Formula('Bilheteria ~ Genero'), data=dados_r, FUN=ro.r['mean'])

# Resultado + df em python 
res_df = pd.DataFrame({
    'Genero': list(res.rx2('Genero')),
    'Bilheteria_media': list(res.rx2('Bilheteria'))
})

print("Média da Bilheteria por Gênero:")
print(res_df)
