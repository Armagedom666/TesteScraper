import pyautogui

# Espere alguns segundos para você mover o mouse para a posição desejada
pyautogui.sleep(5)

# Obtenha as coordenadas atuais do cursor do mouse
x, y = pyautogui.position()

# Exiba as coordenadas
print(f'Coordenadas do cursor do mouse: X={x}, Y={y}')
