import pandas as pd

caminho = './arquivos/entrada/teste1.csv'

df = pd.read_csv(caminho)

df.head()
# print(df.head())

df_cleaned = df.copy()

dropar = [col for col in df_cleaned.columns if "Nome" in col or "E-mai" in col or "Carimbo" in col]
df_cleaned.drop(columns=dropar, axis=1, inplace=True)

column_renames = {
    df_cleaned.columns[0]: "idade",
    df_cleaned.columns[1]: "avaliacao_geral",
    df_cleaned.columns[2]: "principais_aprendizados",
    df_cleaned.columns[3]: "desenvolvimento_pessoal",
    df_cleaned.columns[4]: "impacto_social",
    df_cleaned.columns[5]: "habilidade_lideranca",
    df_cleaned.columns[6]: "habilidade_visao_critica",
    df_cleaned.columns[-10]: "interesse_ciencias_matematica",
    df_cleaned.columns[-9]: "interesse_portugues_ingles",
    df_cleaned.columns[-8]: "conceito_steam",
    df_cleaned.columns[-7]: "conceito_robotica",
    df_cleaned.columns[-6]: "habilidades_a_desenvolver",
    df_cleaned.columns[-5]: "oficina_favorita",
    df_cleaned.columns[-4]: "melhorias_sugeridas",
    df_cleaned.columns[-3]: "preparado_mercado",
    df_cleaned.columns[-2]: "expectativas_atingidas",
    df_cleaned.columns[-1]: "recomendaria"
}

df_cleaned.rename(columns=column_renames, inplace=True)

avaliacao_map = {
    "Excelente: Superou minhas expectativas.": 3,
    "Muito boa: Atendeu às minhas expectativas.": 2,
    "Boa: Foi útil.": 1,
    "Ruim: Não atendeu às minhas expectativas.": 0
}

df_cleaned["avaliacao_geral"] = df_cleaned["avaliacao_geral"].map(avaliacao_map)

df_cleaned["recomendaria"] = df_cleaned["recomendaria"].map({"Sim": 1, "Não": 0})

df_cleaned.head()
print(df_cleaned.head())

df_cleaned.to_csv("./arquivos/limpos/teste1limpo.csv", index=False)