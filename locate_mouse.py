import pyautogui
import time

print("Mova o mouse para o local desejado. As coordenadas aparecerão a cada segundo.\nPressione Ctrl + C para sair.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição atual do mouse: X={x}, Y={y}", end="\r")  # Atualiza na mesma linha
        time.sleep(1)
except KeyboardInterrupt:
    print("\nFinalizado.")
