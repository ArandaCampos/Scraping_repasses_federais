#!/usr/bin/env python

from selenium import webdriver
from time import sleep

estados = ('sp-sao-paulo', 'rj-rio-de-janeiro')

browser = webdriver.Firefox()
for estado in estados:
    html = browser.get(f'https://www.portaltransparencia.gov.br/localidades/{estado}')
    sleep(2)

browser.close()
