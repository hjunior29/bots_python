import pyautogui    #biblioteca que controla mouse e teclado

#fazer um intervalo entre os comendos do pyautogui
pyautogui.PAUSE = 3

#abrir a ferramenta/sistema/programa
pyautogui.press("win")          #apertando a tecla windows
pyautogui.write("login.xlsx")   #escrevendo o arquivo
pyautogui.press("backspace")    #apertando o backspace
pyautogui.press("enter")        #apertando o enter

#preencher o login
pyautogui.click(x=360, y=280)                   #clicando na caixa do login
pyautogui.write("Helder Junior Silva Lima")     #escrevendo o nome de login

#preencher a senha
pyautogui.click(x=360, y=330)   #clicando na caixa de senha
pyautogui.write("********")     #escrevendo a senha

#clicar em fazer login
pyautogui.click(x=360, y=430)   #clicando na caixa do login

#comando para achar as coordenadas dos pixels das caixas, utilizando o mouse na tela
def catch_pixel():
    import pyautogui
    import time                    #biblioteca para pausar os comandos
    time.sleep(3)                  #pausando por 3 segundos
    print(pyautogui.position())    #printando a posição em pixels do mouse na tela

#catch_pixel()