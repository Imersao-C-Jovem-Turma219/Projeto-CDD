from flask import Flask, render_template, jsonify
from peewee import fn
from model import Participante
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/avaliacao_geral")
def avaliacao_geral():
    query = (Participante
             .select(Participante.avaliacao_geral, fn.COUNT(Participante.id).alias('total'))
             .group_by(Participante.avaliacao_geral))
    data = {q.avaliacao_geral: q.total for q in query}
    return jsonify(data)

@app.route("/api/habilidades")
def habilidades():
    campos = [
        'habilidade_lideranca',
        'habilidade_visao_critica',
        'habilidade_inteligencia_emocional',
        'habilidade_criatividade',
        'habilidade_comunicacao',
        'habilidade_trabalho_em_equipe',
        'habilidade_empreendedorismo',
        'habilidade_consciencia_cultural',
        'habilidade_interpretacao_info',
        'habilidade_resolucao_problemas',
        'habilidade_adaptacao',
        'habilidade_tecnologia'
    ]

    resultados = {}
    for campo in campos:
        query = (Participante
                 .select(getattr(Participante, campo), fn.COUNT(Participante.id).alias('total'))
                 .group_by(getattr(Participante, campo)))
        resultados[campo] = {q.__data__[campo]: q.total for q in query}

    return jsonify(resultados)

if __name__ == "__main__":
    os.makedirs("templates", exist_ok=True)
    app.run(debug=True)
