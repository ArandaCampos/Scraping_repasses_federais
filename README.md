## Scraping Repasses Federais


### Sobre

&emsp;Scraping é uma técnica de mineração dados na web, através do qual extraí e converte informações presentes em sites de acesso público em dados estruturados, possibilitando analisá-los e manipulá-los.<br>
&emsp;Neste projeto em específico, foram estraídos os dados dos repasses do governo federal, constantes no portal da transparência, aos estados sudestinos (ES, MG, SP, RJ) nos anos de 2020 à 2022 (sendo no último, extraídos somente os 6 primeiros meses). Em seguida, foram somados e impressos em uma tabela, conforme imagem abaixo

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
