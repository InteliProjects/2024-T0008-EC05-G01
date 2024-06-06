---
title: Artefato - Documentação
sidebar_position: 2
---


## WebCam Qr codes
&emsp;O código qr-code.py (pode ser observado também em Codigo Webcam Qr code), cria um servidor Flask para processar dados de QR codes capturados por uma câmera. Inicialmente, são importadas as bibliotecas necessárias, incluindo Flask para o servidor web, OpenCV para processamento de imagem e TinyDB para armazenamento de dados. Duas instâncias de TinyDB são inicializadas para armazenar informações sobre medicamentos e dados completos dos QR codes.

&emsp;Uma instância do QReader é configurada com parâmetros específicos, como tamanho do modelo e confiança mínima, para lidar com a detecção e decodificação de QR codes. Em seguida, uma função principal chamada “perpetually_read()” é definida. Essa função é responsável por iniciar a câmera, capturar imagens continuamente, detectar QR codes nas imagens e processar os dados dos QR codes encontrados.

&emsp;Outras funções auxiliares também são definidas: “detect_qr_code()” para detectar e decodificar QR codes em um frame de imagem, e “insert_or_update()” para inserir ou atualizar os dados de medicamentos no banco de dados.

&emsp;O servidor Flask é configurado com uma rota “/capture” para fornecer os dados mais recentes dos QR codes capturados. Uma thread é iniciada para executar continuamente a função “perpetually_read()” em segundo plano, lidando com a leitura constante dos QR codes.


&emsp;Sendo assim, para executar o código abordado, o usuário deve seguir algumas etapas simples. Primeiramente, é necessário navegar até a pasta "src" no diretório do projeto e acessar o arquivo qr-code.py. Em seguida, o usuário deve abrir o terminal integrado no ambiente de desenvolvimento do VS Code e ativar o ambiente virtual (venv) necessário para o projeto.

&emsp;Após a ativação do ambiente virtual, o usuário pode iniciar o código executando o seguinte comando no terminal (considerando que está em um ambiente Windows): python .\qr-code.py. Isso iniciará a execução do código e todas as funcionalidades estarão prontas para uso.

&emsp;Se houver a necessidade de executar o código principal responsável pela movimentação do robô, o procedimento é semelhante. O usuário deve garantir que está na pasta "src", inicializar o ambiente virtual e acessar o arquivo main.py. Em seguida, deve-se executar o seguinte comando no terminal integrado do VS Code: python .\main.py.


<p align="center"><b> Codigo Webcam Qr code  </b> </p>

```
from flask import Flask, jsonify
from qreader import QReader
from tinydb import TinyDB, Query
import cv2
import threading
import time
import json

db_medicamentos =TinyDB("db_medicamentos.json")
db = TinyDB("db_completo.json")

# Create a QReader instance
qreader = QReader(
    model_size='l',
    min_confidence=0.5
)

app = Flask(__name__)

# Lista para armazenar os dados dos QR codes
qr_data_lock = threading.Lock()
medicamentos_data_lock = threading.Lock()


def perpetually_read():
    print("Iniciando a câmera")
    camera = cv2.VideoCapture(index=1) # 0 para câmera integrada, 1 para câmera externa
    print("Câmera iniciada")
    last_decoded_text = None  # Variável para armazenar o texto decodificado da última leitura
    try:
        while True:
            _, image = camera.read()

            decoded, time_taken = detect_qr_code(image)

            # Se o tempo de processamento for menor que 0.1 segundos, espere um pouco
            if time_taken < 0.1: time.sleep(0.1)

            if decoded is None: continue # Se nao existir um QR code, continue
            if last_decoded_text == decoded: continue # Se o QR code for o mesmo que o último, continue
            last_decoded_text = decoded # Atualize o último QR code decodificado

            print(f"QR code decodificado: {decoded}")

            # Acha todos os medicamentos com o itemId igual ao QR code decodificado
            with qr_data_lock: medicamentos = db.search(Query().itemId == decoded)

            if medicamentos and len(medicamentos) > 0:
                medicamento = medicamentos[0]

                print(f"Medicamento encontrado: {medicamento}")

                # Adicionando os medicamentos ao nosso banco de dados
                insert_or_update(medicamento)

    except Exception as e: raise e
    finally:
        camera.release()
        print("Câmera liberada")

def detect_qr_code(frame):
    start = time.time()
    decoded_text = qreader.detect_and_decode(image=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if decoded_text and len(decoded_text) > 0 and decoded_text[0] is not None and len(decoded_text[0]) > 0:
        return (decoded_text[0], time.time() - start)
    else: return (None, time.time() - start)

def insert_or_update(medicamento):
    with medicamentos_data_lock: medicamentos = db_medicamentos.search(Query().identificador == medicamento["itemId"])

    if medicamentos and len(medicamentos) > 0:
        with medicamentos_data_lock: db_medicamentos.update({
            "kit": "Kit #?"
        }, Query().identificador == medicamento["itemId"])
    else:
        with medicamentos_data_lock: db_medicamentos.insert({
            "identificador": medicamento["itemId"],
            "kit": "Kit #?"
        })


# Inicie a thread para ler os QR codes
qr_thread = threading.Thread(target=perpetually_read).start()

@app.route('/capture')
def get_qr_data():
    # Retorna os dados mais recentes dos QR codes
    with medicamentos_data_lock: medicamentos = db_medicamentos.all()
    return jsonify({ "dados": medicamentos })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```
<p align="center"><b> Fonte: Elaborado pelos próprios autores </b> </p>

## Documentação do Banco de Dados TinyDB

### Introdução

Esta categoria tem como objetivo descrever como devemos utilizar o banco de dados TinyDB, que é um banco de dados NoSQL que utiliza arquivos JSON para armazenar os dados de uma maneira não relacional. O TinyDB é uma excelente opção para projetos pequenos e médios, pois é simples de utilizar e não requer muita configuração. Por causa de sua natureza não relacional, acabamos criando diversos arquivos JSON para armazenar os dados, que ficam dentro de uma pasta chamada `db`.

### Instalação

Para instalar o TinyDB, basta executar o seguinte comando:

```bash
pip install tinydb
```

Não esqueça de entrar em seu ambiente virtual antes de executar o comando, o que pode ser feito com o comando `source env/bin/activate` ou `./env\Scripts\activate` no Windows após a criação do ambiente virtual com o comando `python -m venv env`.

### Tabelas/Arquivos

O TinyDB não possui tabelas, mas sim arquivos JSON que armazenam os dados. Cada arquivo é uma coleção de documentos, que são os registros do banco de dados. Por exemplo, se quisermos armazenar os dados de um usuário, podemos criar um arquivo chamado `users.json` e armazenar os dados do usuário nesse arquivo. No nosso projeto, temos os seguintes arquivos:

- `kits.json`
- `medicamentos.json`
- `qrcodes.json`

#### Formato de `medicamentos.json`

O arquivo `medicamentos.json` armazena os medicamentos disponíveis no estoque, além das posições aonde eles estão. O formato de um medicamento é o seguinte:

```json
{
    "nome": <str>,		 // Nome do medicamento
    "quantidade": <int>, // Quantidade de medicamentos no estoque
    "pos": {			 // Posição do medicamento no estoque, incluindo:
        "x": <float>,	 // Posição x
        "y": <float>,	 // Posição y
        "z": <float>,	 // Posição z
        "r": <float>	 // Rotação
    }
}
```

#### Formato de `kits.json`

O arquivo `kits.json` armazena os kits, que são conjuntos de medicamentos e as posições aonde eles devem ser colocados. Também armazena a altura do medicamento, que será utilizada para calcular a posição dos próximos medicamentos (assumindo que eles sejam empilhados). O formato de um kit é o seguinte:

```json
{
    "nome": <str>,				 // Nome do kit
    "medicamentos": [			 // Lista de medicamentos no kit
        {						 // Um de vários medicamentos no kit
            "nome": <str>,		 // Nome desse medicamento
            "quantidade": <int>, // Quantidade desse medicamentos no kit
            "altura": <float>,	 // Altura desse medicamento
            "pos": {			 // Posição desse medicamento no kit, incluindo:
                "x": <float>,	 // Posição x
                "y": <float>,	 // Posição y
                "z": <float>,	 // Posição z
                "r": <float>	 // Rotação
            },
        },
        ...
    ]
}
```

#### Formato de `qrcodes.json`

O arquivo `qrcodes.json` armazena os dados dados respectivos aos QR Codes de medicamentos, como o seu identificador e o kit associado. O formato de um QR Code é o seguinte:

```json
{
    "identificador": <str>, // Identificador do QR Code (UUID, por exemplo)
    "kit": <str>			// Nome do kit associado
}
```

### Utilização

Para utilizar o TinyDB, basta importar as classes `TinyDB` e `Query` do módulo `tinydb` e criar um objeto `TinyDB` passando o caminho do arquivo JSON que será utilizado. Por exemplo, para criar um objeto `TinyDB` para o arquivo `medicamentos.json`, basta fazer o seguinte:

```python
from tinydb import TinyDB, Query

medicamentos_db = TinyDB('db/medicamentos.json')
```

Após criar o objeto `TinyDB`, podemos utilizar os métodos `insert`, `update`, `remove` e `search` para manipular os dados. Por exemplo, para inserir um medicamento no banco de dados, podemos fazer o seguinte:

```python
medicamento = {
	"nome": "Paracetamol",
	"quantidade": 100,
	"pos": {
		"x": 1.0,
		"y": 2.0,
		"z": 3.0,
		"r": 4.0
	}
}

medicamentos_db.insert(medicamento)
```

Para buscar medicamentos no banco de dados, podemos utilizar o método `search` passando um objeto `Query` que representa a condição que queremos buscar. Por exemplo, para buscar todos os medicamentos com o nome "Paracetamol", podemos fazer o seguinte:

```python
medicamentos = medicamentos_db.search(Query().nome == "Paracetamol")

for medicamento in medicamentos:
	print(medicamento)
```

Para atualizar um medicamento no banco de dados, podemos utilizar o método `update` passando um objeto `Query` que representa a condição que queremos buscar e um dicionário com os campos que queremos atualizar. Por exemplo, para atualizar a quantidade de todos os medicamentos com o nome "Paracetamol" para 200, podemos fazer o seguinte:

```python
medicamentos_db.update({"quantidade": 200}, Query().nome == "Paracetamol")
```

Também podemos atualizar medicamentos levando um objeto medicamento obtido de uma busca. Por exemplo, para atualizar a quantidade de um medicamento para 200, podemos fazer o seguinte:

```python
medicamento = medicamentos_db.search(Query().nome == "Paracetamol")[0]

medicamento["quantidade"] = 200

medicamentos_db.update(medicamento, Query().nome == "Paracetamol")
```

Para remover um medicamento do banco de dados, podemos utilizar o método `remove` passando um objeto `Query` que representa a condição que queremos buscar. Por exemplo, para remover todos os medicamentos com o nome "Paracetamol", podemos fazer o seguinte:

```python
medicamentos_db.remove(Query().nome == "Paracetamol")
```

## Apresentação Sprint 3
<!-- <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ3qIbOEq8BSlD-ZKAouSGOgQEidCzVeuTL1c-jNZhUR5UxZI9ah9xowzhMtC-csiek5HmO-mDt3J83/pub?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }} ></iframe> -->

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ3qIbOEq8BSlD-ZKAouSGOgQEidCzVeuTL1c-jNZhUR5UxZI9ah9xowzhMtC-csiek5HmO-mDt3J83/embed?start=false&loop=false&delayms=3000" frameborder="0" width="75%" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto' }}></iframe>

<p><b>Fonte:</b> elaborado por Arm </p>