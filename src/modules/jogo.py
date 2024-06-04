import keyboard
import pyautogui
import win32api
import win32con

from modules.temporizadores import pausa_curta

CARACTER_PARADA = 'Q'
COR_PRETA = (0, 0, 0)
COR_VERMELHA = (253, 18, 1)

# Pontos de referência
P1 = (248, 405)
P2 = (313, 405)
P3 = (383, 405)
P4 = (464, 405)

def verfica_cor_na_posicao(posicao: tuple, cor: tuple):
    return pyautogui.pixelMatchesColor(posicao[0], posicao[1], (cor[0], cor[1], cor[2]), tolerance=10)

def click(posicao: tuple):
    win32api.SetCursorPos(posicao)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    pausa_curta()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def inicia_jogo():
    while keyboard.is_pressed(CARACTER_PARADA) == False:
        if verfica_cor_na_posicao(P1, COR_PRETA):
            click(P1)
        if verfica_cor_na_posicao(P2, COR_PRETA):
            click(P2)
        if verfica_cor_na_posicao(P3, COR_PRETA):
            click(P3)
        if verfica_cor_na_posicao(P4, COR_PRETA):
            click(P4)