# INSTRUÇÕES

## REQUISITOS

* Python 3.7+
* pip 20.3+
* pip freeze > requirements.txt
* pip install pytest
* pip install --upgrade pip
* pip install playwright
* playwright install


## ESTRUTURA

### MODELS

* basePage é a classe responsável por comportamentos iterativo.
* com base na BasePage utiliza outra classe para Herdar e gerar comportamentos específicos de um site
* evidences/images são as images geradas pelo metodo generateShot

