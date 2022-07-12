#!/usr/bin/env python

from selenium import webdriver
from time import sleep

# Tuplas contendo os anos e estados pesquisados
anos = ( '2020', '2021', '2022')
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
        repasses = browser.find_element("id", attribute_name)
    except:
        return 0
    if repasses:
        repasses = str(repasses.get_attribute(data_name))
        repasses = repasses.replace('R$', '')
        repasses = repasses.replace('.', '')
        repasses = repasses.replace(',', '.')
        repasses = repasses.replace(' ', '')
        return float(repasses)
    else:
        return 0

# Percorrer as tuplas
for estado in estados:
    print(estado)
    for ano in anos:
        get_transferers_by_id(browser, estado, ano, id_name, data_name)


# Fechar o navegador
browser.close()
