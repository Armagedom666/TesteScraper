import requests
from bs4 import BeautifulSoup

# URL da página da Lotofácil
url = 'https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx'

# Faça uma solicitação GET para obter o conteúdo da página
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parseie o conteúdo HTML da página usando Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre a lista de elementos <li> com a classe especificada
    numeros_sorteio = soup.find_all('li', class_='ng-binding dezena ng-scope')

    # Itere sobre os elementos para obter os números do sorteio
    numeros = [numero.get_text() for numero in numeros_sorteio]

    # Imprima os números do sorteio
    print("Números do Sorteio da Lotofácil:")
    for numero in numeros:
        print(numero)
else:
    print("Falha ao acessar a página da Lotofácil. Verifique a URL ou a conexão com a internet.")
