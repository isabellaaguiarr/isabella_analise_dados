# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv e ncr_ride_regions.xlsx para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento
import pandas as pd 
import requests
import matplotlib.pyplot as plt

arquivo1 = "C:/Users/isabe/Documents/PROJETOS/analise_python_r/dados/ncr_ride_bookings.csv"
df1 = pd.read_csv(arquivo1)

arquivo2 = "C:\\Users\\isabe\\Documents\\PROJETOS\\analise_python_r\\dados\\ncr_ride_regioes.xlsx"
df2 = pd.read_excel(arquivo2)

# 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
filtrando = (df1["Booking Status"] == "Completed")
filtrando.shape
filtro = df1["Booking Status"] == "Completed".sum()

# 2 - Qual a proporção em relação ao total de corridas?
total_corridas = len(df1)
proporcao = filtro / total_corridas

# 3 - Calcule a média e mediana da Distância percorrida por cada Tipo de veículo.
# media
media = df1['Ride Distance'].mean()
media_veiculo = df1.groupby('Vehicle Type')['Ride Distance'].mean()
# media abaixo ou acima 
media_veiculo.min()
media_veiculo.max()
# mediana
mediana = df1.groupby('Vehicle Type')['Ride Distance'].median()

# 4 - Qual o Metodo de Pagamento mais utilizado pelas bicicletas ("Bike") ?
bike = df1['Vehicle Type'].str.strip().str.lower() == 'bike'
payment_bike = df1.loc[bike, 'Payment Method'].value_counts(dropna=True)
mais_usado = payment_bike.idxmax()

# 5 - Faca um merge com ncr_ride_regions.xlsx pela coluna ("Pickup Location") para pegar as regioes das corrifas.
# e verifique qual a Regiao com o maior Valor da corrida?
df1.columns
df2.columns
df_merge_regioes = pd.merge(df1, df2, on="Pickup Location", how="inner")
valor_max = df_merge_regioes.groupby('Regiao')['Booking Value'].max()
valor_max.nlargest(1) 

# 6 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados"
# e filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“venda”).
# Dica Técnica, filtre atraves das coluna FNTSIGLA: df["FNTSIGLA"].str.contains() 
# e depois SERNOME: df["SERNOME"].str.contains() 
# Descubra qual é o código da série correspondente.
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# e construa um DataFrame pandas com as datas (DATA) e os valores (VALVALOR).
# Converta a coluna de datas para o formato adequado (pd.to_datetime())

url_meta = "http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url_meta)
data_meta = response.json()["value"]
df_meta = pd.DataFrame(data_meta)

df_anfavea = df_meta[df_meta["FNTSIGLA"].str.contains("Fipe.*", regex=True, case=False)]
df_imoveis = df_anfavea[df_anfavea["SERNOME"].str.contains("venda", regex=True, case=False)]

SERCODIGO = "FIPE12_VENBR12"  
url_valores = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{SERCODIGO}')"
response = requests.get(url_valores)
data_valores = response.json()["value"]
df = pd.DataFrame(data_valores)

df["VALDATA"] = pd.to_datetime(df["VALDATA"], utc=True, errors="coerce")
df["VALDATA"] = df["VALDATA"].dt.tz_convert("America/Sao_Paulo")
df["DATA"] = df["VALDATA"].dt.date

# 7 -  Monte um gráfico de linha mostrando a evolução das vendas ao longo do tempo.
# Dica: você pode usar a biblioteca matplotlib para gerar o gráfico.
plt.figure(figsize=(12,6))
plt.plot(df["DATA"], df["VALVALOR"], label="Venda de Imoveis", color="blue")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.title("Evolução das Vendas de Imobiliarias- ANFAVEA/IPEA")
plt.legend()
plt.grid(True)
plt.show()


# 8 - Crie o grafico do bitcoin (ticker: "btc") atraves da api preco-diversos
# Pegue o periodo compreendido entre 2001 a 2025
# Monte um gráfico de linha mostrando a evolução do preco de fechamento
# import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNDc4LCJpYXQiOjE3NTYzNzk0NzgsImp0aSI6ImExOTA3MTk5ZTU2NDQ3OGVhNmI0NGJhNDViYzBlYzViIiwidXNlcl9pZCI6IjQ5In0.pZtn2sQhc-GKGZtjWeL6kcZy9RwrJQfKIMZkBak3MTc"
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {
'ticker': 'btc',
'data_ini': '2001-01-01',
'data_fim': '2025-09-01'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/preco-diversos', params=params, headers=headers)
pd.json_normalize(response)
response.status_code
response = response.json()
dados = response["dados"]  
df = pd.DataFrame.from_dict(dados)

colunas = ["ticker", "fechamento" ]  
df_colunas = df[colunas]
colunas_data = ["data"]  
df_colunas_data = df[colunas_data]
df["data"] = pd.to_datetime(df["data"])
plt.figure(figsize=(12,6))
plt.plot( df_colunas_data["data"],df_colunas["fechamento"], label="Evolução do Preco de Fechamento", color="blue")
plt.xlabel("Ano")
plt.ylabel("Preco")
plt.title("Evolução do Preco de Fechamento")
plt.legend()
plt.grid(True)
plt.show()


# 9 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# A autenticação é feita via JWT Token no cabeçalho da requisição.
# Acesse a API no endpoint: https://laboratoriodefinancas.com/api/v1/planilhao
# passando como parâmetro a data (por exemplo, "2025-09-23").
# Construa um DataFrame pandas a partir dos dados recebidos.
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROC (Return on Capital) nessa data.
# Exiba o ticker da empresa, setor e o valor do ROC correspondente.
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNDc4LCJpYXQiOjE3NTYzNzk0NzgsImp0aSI6ImExOTA3MTk5ZTU2NDQ3OGVhNmI0NGJhNDViYzBlYzViIiwidXNlcl9pZCI6IjQ5In0.pZtn2sQhc-GKGZtjWeL6kcZy9RwrJQfKIMZkBak3MTc"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {
'data_base': '2025-09-23'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
pd.json_normalize(response)
response.status_code
response = response.json()
dados = response["dados"]  
df = pd.DataFrame.from_dict(dados)

filtrando = (df["setor"] == "tecnologia") 
colunas = ["ticker", "setor", "roc"] 
maior = df.loc[filtrando, colunas].nlargest(1, 'roc')  
print(maior) 
 
# 10 - A API do Laboratório de Finanças fornece informações de balanços patrimoniais de empresas listadas na B3.
# Acesse o endpoint: https://laboratoriodefinancas.com/api/v1/balanco
# usando a empresa Gerdau ("GGBR4") e o período 2025/2º trimestre (ano_tri = "20252T").
# O retorno da API contém uma chave "balanco", que é uma lista com diversas contas do balanço.
# Localize dentro dessa lista a conta cuja descrição é “Ativo Total” e "Lucro Liquido".
# Calcule o Return on Assets que é dados pela formula: ROA = Lucro Liquido / Ativo Totais
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4OTcxNDc4LCJpYXQiOjE3NTYzNzk0NzgsImp0aSI6ImExOTA3MTk5ZTU2NDQ3OGVhNmI0NGJhNDViYzBlYzViIiwidXNlcl9pZCI6IjQ5In0.pZtn2sQhc-GKGZtjWeL6kcZy9RwrJQfKIMZkBak3MTc"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'ticker': 'GGBR4', 
          'ano_tri': '20252T'
          }
response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
pd.json_normalize(response)
response.status_code
response = response.json()
dados= response["dados"][0]
balanco = dados['balanco']
df = pd.DataFrame(balanco)

ativo_total = df.loc[df["descricao"] == "Ativo Total", "valor"].values[0]
lucro_liquido = df.loc[df["descricao"] == "Lucro Liquido", "valor"].values[0]
roa = lucro_liquido / ativo_total 