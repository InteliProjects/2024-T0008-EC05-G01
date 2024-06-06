from flask import Flask, render_template, request, redirect, json
from tinydb import TinyDB, Query
import time

app = Flask(__name__)

db_data = TinyDB('./db.json')

@app.route('/', methods=['GET', 'POST'])
def index():
    dados = db_data.all()
    return render_template('index.html', dados=dados)

@app.route('/enviando', methods=['POST'])
def envia_dados():
    dados = request.json # ja transforma em json, nao precisa aplicar json.loads
    print(dados)
    # dados = json.loads(dados)
    dado = dados['dado']
    db_data.insert({'dado': dado})
    print({'dado': dado})
    return 'Dado enviado com sucesso!'


@app.route('/dados', methods=['GET'])
def dados():
    dados = db_data.all()
    return json.dumps(dados)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)