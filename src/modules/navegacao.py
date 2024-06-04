import pyautogui
import webbrowser
from pyautogui import ImageNotFoundException

from modules.temporizadores import carregamento_rapido

SITE = 'https://gameforge.com/pt-BR/littlegames/magic-piano-tiles/#'

def abre_site():
    webbrowser.open(SITE)
    carregamento_rapido()

def aceita_cokies():
    try:
        img = pyautogui.locateCenterOnScreen('src/assets/cookies.png')
        pyautogui.click(img[0], img[1], duration=1)
    except ImageNotFoundException:
        pass
    finally:
        carregamento_rapido()