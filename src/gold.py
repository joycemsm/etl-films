import pandas as pd
import boto3
from dotenv import load_dotenv
import os 

load_dotenv()
df = pd.read_csv("data/staging/data_transformed.csv")


decadas = df.groupby((df["Year of Release"] // 10) * 10) 
for ano, grupo in decadas:
    nome_arquivo = f"data/gold/Ano_{ano}_{ano+10}.csv"
    grupo.to_csv(nome_arquivo, index=False)
    print(f"Arquivo salvo: {nome_arquivo} — {len(grupo)} filmes")


s3 = boto3.client("s3", region_name=os.getenv("AWS_REGION"))

for ano, grupo in decadas:
    nome_s3 = f"Ano_{ano}_{ano+10}.csv"
    nome_arquivo = f"data/gold/Ano_{ano}_{ano+10}.csv"
    s3.upload_file(nome_arquivo, os.getenv("BUCKET_GOLD"), nome_s3)
    print(f"Enviado para o S3 Gold: {nome_s3}")