# src/ingest_data.py

import pandas as pd
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus

db_password_raw = "Postgre_vitor_vep07@"
db_nome = "chess_db"
db_usuario = "postgres"
db_host = "127.0.0.1"
db_port = "5432"

#codificando a senha porque pelo visto não pode ter caractere especial no final dela pq da um monte de erro
db_password_encoded = quote_plus(db_password_raw)

# String de conexão que o SQLAlchemy usa para se conectar
database_URL = f"postgresql://{db_usuario}:{db_password_encoded}@{db_host}:{db_port}/{db_nome}"

csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'games.csv')

def ingest_data():
    try:
        # Conectando ao banco de dados
        engine = create_engine(database_URL)
        print("Conexão estabelecida")

        # Carrega os dados do CSV
        print("Lendo dados...")
        df = pd.read_csv(csv_path, sep=',')
        print("Arquivo carregado.")

        # Inserindo os dados na tabela 'games' no banco de dados
        # if_exists='replace': se a tabela já existir, ela será apagada e criada novamente
        # index=False: para não salvar o índice do DataFrame como uma coluna lá nmo SQL
        df.to_sql('games', con=engine, if_exists='replace', index=False)
        print("Dados inseridos")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    ingest_data()