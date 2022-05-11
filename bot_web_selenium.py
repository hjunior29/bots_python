#importa as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def informacoes():
    global categoria
    global pesquisa
    global ordem
    categoria = int(input("Escolha uma categoria:\n\nIPhone(1)\nCelular(2)\nGeladeira(3)\nNotebook(4)\nTV(5)\nOu digite (0) para pesquisar: "))
    if categoria == 0:
        pesquisa = input("")
    ordem = int(input("\n\nOrdenar o produto por:\nMais relevante(1)\nMenor preço(2)\nMaior preço(3)\n"))
    match ordem:
        case 1:
            ordem = 1
        case 2:
            ordem = "price_asc"
        case 3:
            ordem = "price_desc"
    print("\033[0;32mCOLETANDO INFORMAÇÕES...")

#atribui o  webdrive a variável driver e maximiza a janela
#navega até a página da URL
#aguarda 1 segundo para o proximo comando
def abrir_site():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.zoom.com.br/")
    print("\033[0;32mABRINDO O SITE...")
    time.sleep(1)

#identifica a barra de busca na URL e escreve "RX 6600" no campo de pesquisa
#identifica o botão pesquisar e simula o click
def pesquisa_produto():
    if categoria == 0:
        search_box = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/input").send_keys(pesquisa)
        time.sleep(1)
        search_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/button").click()
        time.sleep(1)
        print("\033[0;32mPESQUISANDO O PRODUTO...")
    else:
        escolher_categoria()
        print("\033[0;32mESCOLHENDO A CATEGORIA...")

#filtra o produto
#"menor preço"
def filtrar_produto(): #!!!dando problema
    if ordem != 1:
        drop_down = Select(driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div[2]/select"))
        drop_down.select_by_value(ordem)
    print("\033[0;32mFILTRANDO O PRODUTO...")

def escolher_categoria():
    match categoria:
        case 1:
            select_cat = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/nav/div/a[1]/span").click() #iphone
        case 2:
            select_cat = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/nav/div/a[2]/span").click() #celular
        case 3:
            select_cat = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/nav/div/a[3]/span").click() #geladeira
        case 4:
            select_cat = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/nav/div/a[4]/span").click() #notebook
        case 5:
            select_cat = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/nav/div/a[5]/span").click() #tv

informacoes()
abrir_site()
pesquisa_produto()
filtrar_produto()