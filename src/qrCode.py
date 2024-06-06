from flask import Flask, jsonify
from qreader import QReader
from tinydb import TinyDB, Query
import cv2
import threading
import time
import json

db_medicamentos =TinyDB("db_medicamentos.json")
db = TinyDB("db_completo.json")
# table = db.table("data")

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
    hasRead = False
    print("Iniciando a câmera")
    camera = cv2.VideoCapture(index=1) # 0 para câmera integrada, 1 para câmera externa
    print("Câmera iniciada")
    last_decoded_text = None  # Variável para armazenar o texto decodificado da última leitura
    try:
        while hasRead == False:
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
                global medicamento
                medicamento = medicamentos[0]

                print(f"Medicamento encontrado: {medicamento}")

                # Adicionando os medicamentos ao nosso banco de dados
                insert_or_update(medicamento)
            
            hasRead = True

    except Exception as e: raise e
    finally:
        camera.release()
        print("Câmera liberada")
        return

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
#qr_thread = threading.Thread(target=perpetually_read).start()

@app.route('/capture')
def get_qr_data():
    # Retorna os dados mais recentes dos QR codes
    with medicamentos_data_lock: medicamentos = db_medicamentos.all()
    return jsonify({ "dados": medicamentos })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
