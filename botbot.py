from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Inicializar o navegador
driver = webdriver.Chrome()

# Abrir o YouTube
driver.get("https://www.youtube.com")

# Direcionar o cursor ao campo de pesquisa
search_box = driver.find_element(By.NAME, "search_query")

# Digitar o nome na caixa de pesquisa
search_box.send_keys("Python Tutorials")

search_box.submit()

#espera = WebDriverWait(driver, 10)
#espera.until((EC.presence_of_all_elements_located(By.CSS_SELECTOR, 'video-title')))

#for video in driver.find_element_by(By.CSS_SELECTOR, 'video-title'):
    #print(video.text)
