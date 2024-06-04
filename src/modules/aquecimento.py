import pyautogui
from pyautogui import ImageNotFoundException

from modules.temporizadores import carregamento_rapido

def clica_no_botao_play():
    try:
        x, y = pyautogui.locateCenterOnScreen('src/assets/play.png')
        pyautogui.click(x, y, duration=1, button='left')
    except ImageNotFoundException:
        # Se não encontrar o botão play, tenta clicar no botão de play no local padrão*
        pyautogui.click(354, 445, duration=1, button='left')
    pula_propaganda()

def clica_no_botao_start():
    pyautogui.click(344, 408, duration=1)

def pula_propaganda():
    carregamento_rapido()
    try:
        x, y = pyautogui.locateCenterOnScreen('src/assets/fechar.png')
        pyautogui.click(x, y, duration=1, button='left')
    except ImageNotFoundException:
        x, y = pyautogui.locateCenterOnScreen('src/assets/fechar2.png')
        pyautogui.click(x + 20, y, duration=1, button='left')