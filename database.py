import pandas as pd
from sqlalchemy import create_engine

db_user = 'root'
db_password = '1234'
db_host = 'localhost'
db_name = 'databaseteste1'

connection_string = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'

engine = create_engine(connection_string)

arquivo_csv = './arquivos/limpos/teste1limpo.csv'
df = pd.read_csv(arquivo_csv)

nome_tabela = 'nome_da_tabela'
df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)
