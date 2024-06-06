from machine import Pin, ADC
import utime
import network
import urequests
import ujson
import time
import gc

# Pino GPIO conectado ao sensor óptico reflexivo
pino_sensor = ADC(26)

# Pino GPIO conectado ao LED
pino_led = Pin(13, Pin.OUT)

# Pino GPIO conectado ao buzzer
pino_buzzer = Pin(14, Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Inteli.Iot', '@Intelix10T#')
while not wlan.isconnected() or wlan.status() < 0:
    print("Waiting to connect:")
    time.sleep(1)

meu_ip = wlan.ifconfig()[0]
print(f"IP:{meu_ip}")

servidor = "http://10.128.0.12:8000"

def medir_distancia():
    distancia_total = 0
    for _ in range(3):
        distancia_total += pino_sensor.read_u16()
        utime.sleep(0.1)
    return distancia_total / 3

def detectar_objeto():
    distancia_atual = medir_distancia()
    if distancia_atual < 25000:
        return distancia_atual
    else: return None

def enviar_servidor():
    dist = medir_distancia()
    response = urequests.post(url=f'{servidor}/enviando',
                              headers={'content-type': 'application/json'},
                              json={"dado": dist})
    # print("DADO ENVIADO...")
    print(dist)
    gc.collect()


def detect_loop():
    while True:
        enviar_servidor()
        distancia_inicial = detectar_objeto() # Sempre retorna algo,espera dist<5800
        if distancia_inicial is not None:
            print(f"Objeto detectado e agarrado {distancia_inicial}")
            pino_led.on()
            pino_buzzer.on()
            utime.sleep(0.2)
            pino_buzzer.off()
            pino_led.off()
            
            while medir_distancia() < (distancia_inicial * 1.2):
                enviar_servidor()
                utime.sleep(1)
                
            print("Objeto solto.")
            pino_led.on()
            pino_buzzer.on()
            utime.sleep(0.2)
            pino_buzzer.off()
            pino_led.off()
        else:
            utime.sleep(1)


try:
    detect_loop()
except Exception as e:
    raise e



