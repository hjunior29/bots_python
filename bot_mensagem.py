import pyautogui
import time

pyautogui.PAUSE = 1

mensagem = input("Qual a mensagem que deseja enviar? ")
quantidade = int(input("Quantas vezes deseja enviar? "))

time.sleep(5)

for i in range(quantidade):
    pyautogui.write(mensagem)
    pyautogui.press('enter')