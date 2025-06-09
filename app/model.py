from peewee import *
from database import banco
import pandas as pd
import os
import glob

DATABASE = {
    'name': 'MLdatabase',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': 5432
}

db = PostgresqlDatabase(
    DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port']
)

class BaseModel(Model):
    class Meta:
        database = db


class Participante(BaseModel):
    nome = CharField()
    email = CharField(null=True)
    idade = IntegerField(null=True)
    avaliacao_geral = TextField(null=True)
    contribuicao_programa = TextField(null=True)
    impacto_social = TextField(null=True)
    habilidade_lideranca = CharField(null=True)
    habilidade_visao_critica = CharField(null=True)
    habilidade_inteligencia_emocional = CharField(null=True)
    habilidade_criatividade = CharField(null=True)
    habilidade_comunicacao = CharField(null=True)
    habilidade_trabalho_em_equipe = CharField(null=True)
    habilidade_empreendedorismo = CharField(null=True)
    habilidade_consciencia_cultural = CharField(null=True)
    habilidade_interpretacao_info = CharField(null=True)
    habilidade_resolucao_problemas = CharField(null=True)
    habilidade_adaptacao = CharField(null=True)
    habilidade_tecnologia = CharField(null=True)
    mudancas_online_pos_programa = TextField(null=True)
    perfil_digital = TextField(null=True)
    redes_sociais = TextField(null=True)
    materias_preferidas = TextField(null=True)
    interesse_ciencias_matematica = TextField(null=True)
    interesse_portugues_ingles = TextField(null=True)
    conceito_steam = TextField(null=True)
    conceito_robotica = TextField(null=True)
    habilidades_profissionais_mercado = TextField(null=True)
    atividade_favorita = TextField(null=True)
    atividades_a_melhorar = TextField(null=True)
    sente_preparada = BooleanField(null=True)
    recomendaria = BooleanField(null=True)
    expectativas_atendidas = TextField(null=True)

if __name__ == "__main__":
    db.connect()
    db.create_tables([Participante])

    csv_files = glob.glob('./data/*.csv')

    for csv_path in csv_files:
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df.fillna(value=None, inplace=True)

            for _, row in df.iterrows():
                Participante.create(**row.to_dict())

    db.close()