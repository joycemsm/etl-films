import boto3
from dotenv import load_dotenv
import os 

load_dotenv() 
s3 = boto3.client("s3", region_name=os.getenv("AWS_REGION")) 


s3.upload_file(
    "data/raw/data.csv",
    os.getenv("BUCKET_BRONZE"),
    "data.csv"
)
print("Arquivo raw enviado para o Bronze com sucesso!")

s3.upload_file(
    "data/staging/data_transformed.csv",
    os.getenv("BUCKET_SILVER"),
    "data_transformed.csv"
)
print("Arquivo transformado enviado para o Silver com sucesso!")