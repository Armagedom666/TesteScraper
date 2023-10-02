from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


driver = webdriver.Edge()

try:
    # Abra o site do YouTube
    driver.get("https://www.youtube.com")

    # Aguarde até que o campo de pesquisa esteja visível
    search_box = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.NAME, "search_query"))
    )

    # Insira um termo de pesquisa
    search_box.send_keys("gentleman")

    #Pressione Enter para iniciar a pesquisa
    search_box.send_keys(Keys.RETURN)

    # Aguarde alguns segundos (você pode ajustar esse valor conforme necessário)
    driver.implicitly_wait(5)
except TimeoutException as e:
    print("O elemento de pesquisa não foi encontrado. Verifique a página ou o código.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {str(e)}")

