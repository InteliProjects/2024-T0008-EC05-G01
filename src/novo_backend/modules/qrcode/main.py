import time

import cv2
from pubsub import pub
from qreader import QReader
from tinydb import Query

from database.wrapper import DB

qreader = QReader(
    model_size='l',
    min_confidence=0.5
)


def perpetually_read():
    print("Iniciando a câmera")
    camera = cv2.VideoCapture(index=2) # 0 para câmera integrada do laptop, 1 para câmera externa conectada via usb.
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
            last_decoded_text = decoded

            print(f"QR code decodificado: {decoded}")
            pub.sendMessage("camera_data", data=decoded)

            # Acha todos os medicamentos com o itemId igual ao QR code decodificado
            with DB("database/archives/qrcode/db_completo.json") as db:
                medicamentos = db.search(Query().itemId == decoded)

            if medicamentos and len(medicamentos) > 0:
                medicamento = medicamentos[0]

                print(f"Medicamento encontrado: {medicamento}")

                # Adicionando os medicamentos ao nosso banco de dados
                insert_or_update(medicamento)

    except Exception as e: raise e
    finally:
        camera.release()
        print("Câmera liberada")

def detect_qr_code(frame: cv2.typing.MatLike):
    start = time.time()
    decoded_text = qreader.detect_and_decode(image=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if decoded_text and len(decoded_text) > 0 and decoded_text[0] is not None and len(decoded_text[0]) > 0:
        return (decoded_text[0], time.time() - start)
    else: return (None, time.time() - start)

def insert_or_update(medicamento):
    with DB("database/archives/qrcode/db_medicamentos.json") as db_medicamentos:
        medicamentos = db_medicamentos.search(Query().identificador == medicamento["itemId"])

    if medicamentos and len(medicamentos) > 0:
        with DB("database/archives/qrcode/db_medicamentos.json") as db_medicamentos:
            db_medicamentos.update({
                "kit": "Kit #1"
            }, Query().identificador == medicamento["itemId"])
    else:
        with DB("database/archives/qrcode/db_medicamentos.json") as db_medicamentos:
            db_medicamentos.insert({
                "identificador": medicamento["itemId"],
                "kit": "Kit #1"
            })