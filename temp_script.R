
library(readxl)

# Ler o arquivo Excel
dados <- read_excel("C:\Users\isabe\Documents\PROJETOS\isabella_analise_dados\data\filmes.xlsx")

# Exemplo de análise: resumo estatístico
resumo <- summary(dados)
print(resumo)
