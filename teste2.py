import json
from selenium import webdriver

# Carregue o arquivo JSON
with open('scrapeLoto.json', 'r') as file:
    data = json.load(file)

# Inicialize o driver do navegador
driver = webdriver.Chrome()  # Você deve ter o ChromeDriver instalado e no PATH

# Loop através dos testes no arquivo JSON
for test in data['tests']:
    print(f'Executando teste: {test["name"]}')
    driver.get(data['url'])  # Abre a URL especificada

    # Execute os comandos no teste atual
    for command in test['commands']:
        cmd = command['command']
        target = command['target']
        if cmd == 'open':
            driver.get(target)
        elif cmd == 'click':
            element = driver.find_element_by_css_selector(target)
            element.click()
        elif cmd == 'setWindowSize':
            width, height = target.split('x')
            driver.set_window_size(int(width), int(height))
        # Adicione mais casos para outros comandos conforme necessário

# Feche o navegador após a conclusão dos testes
driver.quit()
