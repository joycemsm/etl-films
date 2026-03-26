<<<<<<< HEAD
# Pipeline de Dados — Filmes IMDb

## Sobre o projeto
Pipeline de engenharia de dados que extrai, transforma e carrega dados de filmes do IMDb seguindo a Arquitetura Medalhão na AWS S3.

## Tecnologias utilizadas
- Python 3.13
- Pandas
- Boto3
- AWS S3
- AWS VPC
- uv

## Arquitetura
- **Bronze** — dado bruto original
- **Silver** — dado limpo e transformado
- **Gold** — dado particionado por década

## Transformações realizadas
- Remoção das colunas: MetaScore, Gross, Certification
- Verificação e remoção de filmes sem nome
- Adição da coluna data_extracao
- Particionamento por década na camada Gold

## Infraestrutura AWS
- Região: us-east-1 (Virgínia)
- VPC com 2 Availability Zones
- Subnets públicas e privadas
- Cross-Region Replication para sa-east-1 (São Paulo)

## Como executar
```bash
# Instalar dependências
uv sync

# Transformar os dados
uv run src/transform.py

# Subir para o S3
uv run src/upload_s3.py

# Gerar camada Gold
uv run src/gold.py
```

## Estrutura do projeto
```
imdb-pipeline/
  data/
    raw/        ← dado original
    staging/    ← dado transformado
    gold/       ← dado particionado por década
  src/
    transform.py
    upload_s3.py
    gold.py
  notebooks/
    explore.ipynb
```
=======
# etl-films
>>>>>>> 5346b73aa115c6f3b14a3a5c570a45cc195f62f1
