# Versao sem arquivo 
import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri, conversion

# Criar os dados no Python
dados_python = pd.DataFrame({
    "Filme": ["Filme A", "Filme B", "Filme C", "Filme D", "Filme E"],
    "Genero": ["Ação", "Comédia", "Ação", "Comédia", "Ação"],
    "Bilheteria": [100, 150, 200, 120, 250]
})

print("Dados originais no Python:")
print(dados_python)
print("\n")

# Convertendo os dados para R
aggregate = ro.r['aggregate']

with conversion.localconverter(ro.default_converter + pandas2ri.converter):
    dados_r = ro.conversion.py2rpy(dados_python)  # Converte pandas -> R
    res = aggregate(ro.Formula('Bilheteria ~ Genero'), data=dados_r, FUN=ro.r['mean'])

# Resultados 
print("Média da Bilheteria por Gênero calculada no R:")
print(res)