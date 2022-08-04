#!/usr/bin/env python
from selenium import webdriver
from time import sleep
from decorator import retry
import pandas as pd
import locale
import re

# Tuplas contendo os anos e estados pesquisados
years = ('2020', '2021', '2022')
states = ('sp-sao-paulo', 'rj-rio-de-janeiro', 'mg-minas-gerais', 'es-espirito-santo')

# Variáveis auxiliares para busca
names_tags = ('recursosTransferidosAoGovernoEstadual','gastosDiretosGovernoFederalNaLocalidade', 'beneficiosNaLocalidade')
names_data = 'data-original-title'

# Instânica webdriver
browser = webdriver.Firefox()
request_for_minutes = 4

# Arrays para os dados extraídos
columns = ('Valores Transferidos', 'Gastos Diretos', 'Benefícios aos cidadãos', 'Total repassado')
titles = ('São Paulo (SP)', 'Rio de Janeiro (RJ)', 'Minas Gerais (MG)', 'Espirito Santo (ES)')

@retry(repeat=5, secounds=120)
def get_transferers_by_id(browser, state, year, name_attribute):
    """
    Pega o valor transferido para o estado

    Argumentos:
        - browser = Instânica do webdriver
        - state = Estado pesquisado. Ex: sp-sao-paulo
        - year = Ano de pesquisa. Ex: 2020
        - name_attributes = Nome do id da tag que contém o dado
        - names_data = Nome do atributo que contém o dado
    """

    try:
        browser.get(f'https://www.portaltransparencia.gov.br/localidades/{state}?ano={year}')
        value = browser.find_element("id", name_attribute).get_attribute(names_data)
    except:
        return 0
    return value

def summation(texts):
    """
    Extrai o float do texto. Ex: R$1.000,00 -> 1000.00

    Argumentos:
        textos: lista de textos que contém o valor float a ser extraido
    """
    total = 0.0
    # Configurando o locale para Reais
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    for text in texts:
        value = str(text)
        value = re.sub(r'[^0-9,]', '', value)
        value = value.replace(',', '.')
        total += float(value)
    total = locale.currency(total)
    return total

def create_table(state, rows):
    """
    Cria e imprime um DataFrame

    Argumentos:
        - state: Nome do estado a ser imprimido
        - rows: Lista de linhas da tabela
    """
    df = pd.DataFrame(data=rows, index=years, columns=columns)
    print('\n----------- ' + state + '-----------\n')
    print(df)


# Percorrer as tuplas
if __name__ == '__main__':
    for index, state in enumerate(states):
        rows = []
        for year in years:
            data = []
            for tag in names_tags:
                data.append(get_transferers_by_id(browser, state, year, tag))
            data.append(summation(data))
            rows.append(data)
            # T = 1 / f * 60s (por minuto)
            sleep(60 / request_for_minutes)

        create_table(titles[index], rows)

# Fechar o navegador
browser.close()
