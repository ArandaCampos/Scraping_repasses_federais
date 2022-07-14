## Scraping Repasses Federais
![Badge de licença](http://img.shields.io/static/v1?label=LICENÇA&message=GNU&color=sucess&style=for-the-badge)   ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=sucess&style=for-the-badge)   ![Badge versionamento](http://img.shields.io/static/v1?label=VERSAO&message=1.0&color=sucess&style=for-the-badge)

### Sobre

&emsp;`Web Scraping` é uma técnica de mineração dados na qual extrai informações de sites público e converte-os em dados estruturados, possibilitando analisá-los e manipulá-los.<br>
&emsp;Em específico neste projeto, foram estraídos os dados do portal da transparência sobre os repasses do governo federal aos estados sudestinos (ES, MG, SP, RJ) nos últimos 3 anos (2020, 2021, 2022). Em seguida, foram contabilizados e imprimidos em uma tabela (DataFrame), conforme imagem abaixo

### Bora ver como o projeto ficou?

![scraping_repasses_federais](https://user-images.githubusercontent.com/87876734/178601506-669199ed-b6c0-4c0e-a445-2f4099258b8f.png)

### Pré-requisitos

  - Python >= 3.8
  - Geckodrive
  
### Instalação
  
    # Clone o repositório
    >> mkdir Scraping_repasses_federais
    >> git clone https://github.com/ArandaCampos/Scraping_repasses_federais.git Scraping_repasses_federais/

    # Crie um ambiente virtual
    >> cd Scraping_repasses_federais
    >> virtualenv .
    >> source bin/activate

    # Instale as dependências
    (Scraping_repasses_federais) >> pip install -r requirements.txt
    
    # Rode o código
    (Scraping_repasses_federais) >> python src/main.py
  
### Tecnologias empregadas
  - Python
  - Selenium
  - Pandas
