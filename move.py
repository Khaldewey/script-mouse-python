import pyautogui
import time

def mover_mouse(x, y):
    pyautogui.moveTo(x, y)

while True:
    # Exemplo: mover o mouse para as coordenadas (500, 500)
    mover_mouse(500, 500)

    # Aguarda 5 segundos antes de continuar
    time.sleep(5)

    # Exemplo: mover o mouse para as coordenadas (700, 700) após o atraso
    mover_mouse(700, 700)
