#!/usr/bin/env python
from selenium import webdriver
from time import sleep
import re

# Tuplas contendo os anos e estados pesquisados
anos = ('2020', '2021', '2022')
estados = ('sp-sao-paulo', 'rj-rio-de-janeiro', 'mg-minas-gerais', 'es-espirito-santo')

# Variáveis auxiliares para busca
id_name = 'recursosTransferidosAoGovernoEstadual'
data_name = 'data-original-title'

# Instânica webdriver
browser = webdriver.Firefox()

def get_transferers_by_id(browser, estado, ano, attribute_name, data_name):
    """
    Pega o valor transferido para o estado

    Argumentos:
        - browser = Instânica do webdriver
        - estado = Estado pesquisado. Ex: sp-sao-paulo
        - ano = Ano de pesquisa. Ex: 2020
        - attribute_name = Nome do id da tag que contém o dado
        - data_name = Nome do atributo que contém o dado
    """

    try:
        browser.get(f'https://www.portaltransparencia.gov.br/localidades/{estado}?ano={ano}')
        repasses = browser.find_element("id", attribute_name).get_attribute(data_name)
    except:
        return 0
    return repasses

def parse_text_float(text):
    """
    Extrai o float do texto. Ex: R$1.000,00 -> 1000.00

    Argumentos:
        text: texto que contém o valor float a ser extraido
    """
    string = str(text)
    string = re.sub(r'[^0-9,]', '', string)
    string = string.replace(',', '.')
    return float(string)


# Percorrer as tuplas
for estado in estados:
    print(estado)
    for ano in anos:
        text = get_transferers_by_id(browser, estado, ano, id_name, data_name)
        value = parse_text_float(text)
        print(value)

# Fechar o navegador
browser.close()
