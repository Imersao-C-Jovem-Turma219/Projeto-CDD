import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    'name' : os.getenv("DB_NAME"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT"))
}

banco = PostgresqlDatabase(DATABASE)
