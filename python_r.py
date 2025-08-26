import subprocess, os

arquivo_excel = "C:\\Users\\isabe\\Documents\\PROJETOS\\isabella_analise_dados\\data\\filmes.xlsx"

comandos_r = f"""
library(readxl)
dados <- read_excel("{arquivo_excel}")
print(summary(dados))
"""

arquivo_temp_r = "temp_script.R"
with open(arquivo_temp_r, "w") as f:
    f.write(comandos_r)

subprocess.run(["Rscript", arquivo_temp_r], check=True)
os.remove(arquivo_temp_r)

