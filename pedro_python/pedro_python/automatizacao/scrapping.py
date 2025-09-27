
# biblioteca de requisição

import requests

# Responsável por tratar o retorno

from bs4 import BeautifulSoup

# pip install request
# pip install bs4

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = "https://www.netshoes.com.br/busca?nsCat=Natural&q=tenis&mi=hm_sc_ccName__tj_gen_tenis&psn=Banner_Tarja&sort=best-sellers"

# fazendo requisição http

resposta = requests.get(url, headers=headers)

# verifica se deu certo

if resposta.status_code == 200:
    print("Requisição feita com sucesso")
    # 200 - OK

    # traduzir a resposta do site

    soup = BeautifulSoup(resposta.text, "html.parser")

    # Recortar a informação especifíca 

    tenis = soup.find_all("h2", class_="card__description--name")

    print("Ultimas novidadesss")
    for teni in tenis:
        print(f'{teni}')
          