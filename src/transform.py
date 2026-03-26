# --------------------------------------------------------------------

import pandas as pd
from datetime import date

# EXTRACT

df = pd.read_csv("data/raw/data.csv", index_col=0)

# TRANSFORM

sem_nome = df[df["Movie Name"].isnull()]
print(sem_nome) 

if sem_nome.empty:
     print("Nenhuma linha sem nome encontrada.")
else:
    print("Linhas sem nome encontradas:")
    print(sem_nome)
    df = df.dropna(subset=["Movie Name"])

df = df.drop(columns=["MetaScore", "Gross", "Certification"])
print(df.head())

df["data_extracao"] = date.today().isoformat()
print(df.head())

# LOAD

df.to_csv("data/staging/data_transformed.csv", index=False)
print("Arquivo salvo em staging com sucesso!")
print(f"Total de linhas: {len(df)}")
        