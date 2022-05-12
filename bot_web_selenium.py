#importando as bibliotecas
import pandas as pd                                 #biblioteca de importação do arquivo .csv
from bs4 import BeautifulSoup                       #biblioteca de varredura de dados
from selenium import webdriver                      #biblioteca para controlar o navegador
from selenium.webdriver.common.by import By         #algumas funcionalidades da biblioteca
from selenium.webdriver.common.keys import Keys     #algumas funcionalidades da biblioteca
import time                                         #biblioteca de tempo

#define todas as variáveis globais que serão usadas a frente
#oferece a escolha de um atalho por categorias
#pega informações do usuário sobre o produto buscado
#e sobre a ordem que os produtos vão aparecer
#o usuário escolhe o nome do arquivo .csv
def pegar_informacoes():
    global categoria
    global pesquisa
    global ordem
    global nome_arquivo
    categoria = int(input("Escolha uma categoria:\nIPhone(1)\nCelular(2)\nGeladeira(3)\nNotebook(4)\nTV(5)\nOu digite (0) para pesquisar: "))
    if categoria == 0:
        pesquisa = input("Pesquisar:\n")
    ordem = int(input("\n\nOrdenar o produto por:\nMais relevante(1)\nMenor preço(2)\nMaior preço(3)\n"))
    nome_arquivo = input("\nQual vai ser o nome do arquivo .csv: ")

#declara a variável driver global
#atribui o webdriver a variável driver
#maximiza a janela
#navega até a página da URL
def abrir_site():
    print("\n\033[1;33mABRINDO O SITE...")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.zoom.com.br/")
    print("\033[0;32mSITE ABERTO.")

#condiciona para caso o usuário escolha digitar a pesquisa ou caso escolha uma das categorias
#caso o usuário escolha dgitar, a função identifica a barra de busca do site
# e escreve a pesquisa do usuário e identifica o botão pesquisar e simula o click
#caso o usuário escolha uma categoria, a função vai chamar outra
def pesquisar_produto():
    if categoria == 0:
        print("\033[1;33mPESQUISANDO O PRODUTO...")
        search_box = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/input").send_keys(pesquisa)
        time.sleep(1)
        search_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/button").click()
        time.sleep(3)
        print("\033[0;32mPRODUTO PESQUISADO.")
    else:
        print("\033[1;33mESCOLHENDO A CATEGORIA...")
        escolher_categoria()

#identifica a categoria que o usuário escolheu
#e simula um click em cima da categoria
def escolher_categoria():
    select_cat = driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div[4]/div/nav/div/a[{categoria}]/span").click()
    print("\033[0;32mCATEGORIA ESCOLHIDA.")

#filtra os produtos pela ordem que o usuário escolheu
#usando uma função da biblioteca de simulação de teclas do teclado
def filtrar_produto():
    print("\033[1;33mFILTRANDO O PRODUTO...")
    ordenar = driver.find_element(By.ID, "orderBy").click()
    time.sleep(1)
    if ordem == 2:
        seta = driver.find_element(By.ID, "orderBy").send_keys(Keys.DOWN)
        time.sleep(1)
    elif ordem == 3:
        seta = driver.find_element(By.ID, "orderBy").send_keys(Keys.DOWN)
        seta = driver.find_element(By.ID, "orderBy").send_keys(Keys.DOWN)
        time.sleep(1)
    enter = driver.find_element(By.ID, "orderBy").send_keys(Keys.ENTER)

#parsea o HTML por meio do BeautifulSoup
def parsear():
    global soup
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, "html.parser")

#coleta os dados da página
def coletar_dados():
    global list_products
    products = soup.findAll(class_="Cell_Infos__KDy41")
    list_products = []
    for product in products:
        product_name = product.find(class_="Text_Text__VJDNU Text_LabelSmRegular__qvxsr")
        product_price = product.find(class_="Text_Text__VJDNU Text_LabelMdBold__uMr7_ CellPrice_MainValue__JXsj_")
        list_products.append([product_name.text, product_price.text])

#cria um DataFrame e aloca os dados em um arquivo .csv
def criar_csv():
    products_data = pd.DataFrame(list_products, columns=["Nome do Produto",  "Preço"])
    products_data.to_csv(f"{nome_arquivo}.csv", index=False)
    print("\033[0;32m"+products_data)

    print("\n\033[0;32mPROCESSO FINALIZADO")



#chamando cada função na ordem
pegar_informacoes()
abrir_site()
pesquisar_produto()
filtrar_produto()
parsear()
coletar_dados()
criar_csv()


#outra opção da função de escolher a categoria
def escolher_categoria2():
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
    print("\033[0;32mCATEGORIA ESCOLHIDA.")

#outra opção da função de filtrar o produto
#é menor, porém quebra mais fácil
def filtrar_produto2():
    print("FILTRANDO O PRODUTO...")
    if ordem == 2:
        ordenar_menor = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/select/option[2]").click()
    elif ordem == 3:
        ordenar_maior = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/select/option[3]").click()
    print("\033[0;32mPRODUTO FILTRADO.")

#tentativa de função para passar a página
def passar_pagina(): #dando erro!!!
    for i in range(4):
        passar = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[4]/div/ul/li[6]/a").click()