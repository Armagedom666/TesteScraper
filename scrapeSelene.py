from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicialize o navegador
driver = webdriver.Chrome()

# URL da página da Lotofácil
url = 'https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx'

# Acesse a página
driver.get(url)

try:
    # Aguarde até que os números do sorteio sejam carregados
    numeros_sorteio = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'ng-binding dezena ng-scope'))
    )

    # Extraia os números do sorteio
    numeros = [numero.text for numero in numeros_sorteio]

    # Imprima os números do sorteio
    print("Números do Sorteio da Lotofácil:")
    for numero in numeros:
        print(numero)
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    # Feche o navegador quando terminar
    driver.quit()
