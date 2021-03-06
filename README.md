# IOWA Liquor Sales Data Exploration and Analysis

Esse dataset é uma junção dos registros de vendas de bebidas alcóolicas no estado do Iowa, Estados Unidos da América. Nesse estado, todas as vendas devem ser registradas por determinação legal. Os dados contém informações relevantes as quais podem ser exploradas. No entanto, é um dataset muito grande e difícil de ser manipulado na forma em que é disponibilizado. Assim, é necessário fazer um tratamento e escolha dos dados a serem utilizados, para facilitar análise. Há uma grande quantidade de dados geográficos e nomes de cidades e condados que precisam ser examinados. Outra dificuldade é entender a geografia local, pois trata-se de um outro país com organizações geográficas diferentes do nosso. Acreditamos que todos esses dados poderiam ser apresentados de uma melhor forma, facilitando o entendimento. 
 [Acesso ao dataset](https://www.kaggle.com/residentmario/iowa-liquor-sales/version/2)
 ## 
 ![png](/src/img/g1239.png)
 ## 

## Objetivos e resultados chave
- Identificar variáveis
- Realizar análise exploratória dos dados
  - Retirar linhas vazias
  - Uniformizar os dados
  - Encontrar os condados onde se vendeu mais
  - No condado onde se vendeu mais, quais cidades venderam mais bebida
  - Encontrar as cidades onde se vendeu mais
  - Saber em que ano nos dados disponíveis houve maior venda de bebidas
- Criar modelo de detecção de melhores locais para iniciar vendas de bebidas

## Conteúdo
- init.ipynb: Análise exploratória de dados
- processing.ipynb: utilização de amostra com slugfication
- var_classes.ipynb: classificação das variáveis

## Pré-Requisitos
- Python 3.8+
- Poetry (Opcional, porém recomendado)
- Obter credenciais do Kaggle API. 
  - [Kaggle API Docs](https://github.com/Kaggle/kaggle-api#api-credentials) 

## Instalação
### Instalação das dependências utilizando Poetry:
- Executar `poetry install`;
- Para entrar na virtualenv do poetry, basta executar `poetry shell`;

### Instalação através do arquivo setup.py
- Criar uma venv executando: `python -m venv .venv`;
- Entrar na venv:
  - Linux: `source .venv/bin/activate`;
  - Windows: `.venv\Scripts\activate`.
- Executar o comando `python setup.py install`.

## Obtenção do Dataset
- Executar: `inv get-dataset`. O dataset será salvo em `data/raw/`.

## Geração do build
### Gerando build através do Poetry:
- Executar `poetry build`. Build será salvo em dist/
- Para instalar o build basta executar `pip install dist/iwoalicor-...-.whl`

## Utilização
- Bibliotecas:
  - [MatplotLib](https://matplotlib.org/)
  - [Numpy](https://numpy.org/)
  - [Pandas](https://pandas.pydata.org/)
  - [Slugify](https://pypi.org/project/python-slugify/)
  - [SciKit-Learn](https://scikit-learn.org/stable/)
- Ferramentas
  - [Jupyter](https://jupyter.org/)
  - [Anaconda](https://www.anaconda.com/)
## Desenvolvedores

 - [André Rodrigues](http://github.com/andrerodrig)
 - [Antonio José](http://github.com/ajsalmeida)
