# Revisao Indicadores
 
# 1 - Voc� tem acesso � API do Laborat�rio de Finan�as, que fornece dados do Planilh?o em formato JSON. 
# A autentica�?o � feita via JWT Token no cabe�alho da requisi�?o.
# Acesse a API no endpoint: https://laboratoriodefinancas.com/api/v1/planilhao
# passando como par�metro a data do dia de hoje (por exemplo, "2025-09-17").
# Construa um DataFrame pandas a partir dos dados recebidos.
# Selecione a empresa que apresenta o maior ROE (Return on Equity) nessa data.
# Exiba o nome da empresa e o valor do ROE correspondente.

import pandas as pd
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNDc4LCJpYXQiOjE3NTYzNzk0NzgsImp0aSI6ImExOTA3MTk5ZTU2NDQ3OGVhNmI0NGJhNDViYzBlYzViIiwidXNlcl9pZCI6IjQ5In0.pZtn2sQhc-GKGZtjWeL6kcZy9RwrJQfKIMZkBak3MTc"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {
'data_base': '2025-09-17'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
pd.json_normalize(response)
response.status_code
response = response.json()
dados = response["dados"]  
df = pd.DataFrame.from_dict(dados)

# Filtrando o top01
colunas = ["ticker", "data_base", "roe"]  
top01 = df[colunas].nlargest(1, 'roe')  
print(top01)


# 2 - Acesse a API do Planilh?o e traga os dados de uma data de sua escolha.
# Construa um DataFrame pandas com os dados recebidos.
# Filtre as empresas que pertencem ao setor ?petr�leo?.
# Elimine todos os registros cujo indicador P/VP (p_vp) seja negativo.
# Selecione a empresa com o maior P/VP dentro do setor de petr�leo e exiba seu ticker, setor e valor de P/VP.

import pandas as pd
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNDc4LCJpYXQiOjE3NTYzNzk0NzgsImp0aSI6ImExOTA3MTk5ZTU2NDQ3OGVhNmI0NGJhNDViYzBlYzViIiwidXNlcl9pZCI6IjQ5In0.pZtn2sQhc-GKGZtjWeL6kcZy9RwrJQfKIMZkBak3MTc"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {
'data_base': '2025-09-17'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
pd.json_normalize(response)
response.status_code
response = response.json()
dados = response["dados"]  
df = pd.DataFrame(dados)

# Filtrando 
filtrando = (df["setor"] == "petróleo") & (df["p_vp"] > 0) 
colunas = ["ticker", "setor", "p_vp"] 
maior = df.loc[filtrando, colunas].nlargest(1, 'p_vp')  
print(maior) 


# 3 - A API do Laborat�rio de Finan�as fornece informa�?es de balan�os patrimoniais de empresas listadas na B3.
# Acesse o endpoint: https://laboratoriodefinancas.com/api/v1/balanco
# usando o ticker PETR4 e o per�odo 2025/2� trimestre (ano_tri = "20252T").
# O retorno da API cont�m uma chave "balanco", que � uma lista com diversas contas do balan�o.
# Localize dentro dessa lista a conta cuja descri�?o � ?1 - Ativo Total?.
# Exiba o valor correspondente a essa conta.

import pandas as pd
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNDc4LCJpYXQiOjE3NTYzNzk0NzgsImp0aSI6ImExOTA3MTk5ZTU2NDQ3OGVhNmI0NGJhNDViYzBlYzViIiwidXNlcl9pZCI6IjQ5In0.pZtn2sQhc-GKGZtjWeL6kcZy9RwrJQfKIMZkBak3MTc"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'ticker': 'PETR4', 
'ano_tri': '20252T'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
pd.json_normalize(response)
response.status_code
response = response.json()
dados= response["dados"][0]
balanco = dados['balanco']
df = pd.DataFrame(balanco)

# Filtro 
ativo_total = df.loc[df["descricao"] == "Ativo Total", "valor"].values[0]
print("Ativo Total:", ativo_total)

# ativo_total = df.loc[(df["descricao"] == "Ativo Total") & (df["conta"] == "1"),"valor"]
# print(ativo_total)
