#importa as bibliotecas
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1.Inicia o navegador e o processo de pesquisa
search_text = input("Pesquisa:  ")
pages = int(input("Raspar quantas páginas: "))
file_name = input("Nome do arquivo .csv: ")
driver = webdriver.Chrome()
driver.maximize_window()
print(f"\n\033[1;mABRINDO O SITE...")
url = "https://www.zoom.com.br/"
driver.get(url)
time.sleep(1)
search_box = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/input").send_keys(search_text)
time.sleep(1)
print(f"\033[1;mPESQUISANDO O PRODUTO...")
search_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/button").click()
time.sleep(3)

# 2.Parsea o HTML por meio do BeautifulSoup
page_content = driver.page_source
soup = BeautifulSoup(page_content, "html.parser")

# 3.Coleta os dados de cada página
products = soup.findAll(class_="Cell_Infos__KDy41")
list_products = []
for i in range(1, (pages+1)):
    driver.get(f"https://www.zoom.com.br/search?q={search_text}&page={i}")
    print(f"RASPANDO PÁGINA {i}")
    # 3.1 Evita raspar páginas em branco
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[2]/div")
    except:
        pass
    else:
        print(f"\033[1;31mNÃO HÁ PRODUTOS PARA RASPAR DA PÁGINA {i} EM DIANTE\033[0;0m")
        break
    time.sleep(2)
    for product in products:
        product_name = product.find(class_="Text_Text__VJDNU Text_LabelSmRegular__qvxsr")
        product_price = product.find(class_="Text_Text__VJDNU Text_LabelMdBold__uMr7_ CellPrice_MainValue__JXsj_")
        list_products.append([product_name.text, product_price.text])

# 4.Cria um DataFrame e aloca os dados em um arquivo .csv
products_data = pd.DataFrame(list_products, columns=["Nome do Produto",  "Preço"])
products_data.to_csv(f"{file_name}.csv", index=False, sep=';', encoding="utf-8")
print("\n", products_data)
print("\n\033[0;32mPROCESSO FINALIZADO")