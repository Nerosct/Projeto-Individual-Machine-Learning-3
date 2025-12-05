# Projeto Prático – Análise e Predição de Vendas Globais de Video Games

## 1. Descrição do Projeto

Este projeto tem como objetivo aplicar técnicas de análise de dados, engenharia de atributos e modelagem preditiva utilizando um conjunto de dados de vendas de jogos eletrônicos. A proposta integra conceitos de ETL, análise exploratória, aprendizado de máquina e visualização de resultados, conforme solicitado no Projeto Prático da disciplina.

O dataset utilizado contém informações de vendas por região, plataforma, gênero e editora, permitindo a criação de um modelo para prever o volume de vendas globais de um jogo.

---

## 2. Estrutura do Projeto

```
project/
│
├── data/
│   ├── raw/
│   │   └── video_games_sales.csv
│   └── processed/
│
│
├── src/
│   ├── etl/
│   │   ├── load.py
│   │   ├── clean.py
│   │   └── transform.py
│   │
│   ├── eda/
│   │   └── visualizations.py
│   │
│   ├── ml/
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   └── evaluate.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## 3. Processo de ETL

### Extração

Os dados são carregados a partir do arquivo `video_games_sales.csv`, contendo as seguintes informações:

* Rank
* Name
* Platform
* Year
* Genre
* Publisher
* NA_Sales
* EU_Sales
* JP_Sales
* Other_Sales
* Global_Sales

### Limpeza

As seguintes etapas são realizadas:

* Conversão de tipos numéricos
* Ajuste e padronização de colunas
* Remoção de registros inconsistentes
* Tratamento de valores ausentes
* Normalização de nomes de publishers e plataformas

### Transformação

São criadas features derivadas, como:

* Soma regional de vendas
* Percentual de vendas por região
* Ranking por gênero
* Codificação categórica de variáveis

Os dados finais são salvos em `data/processed/`.

---

## 4. Análise Exploratória

A EDA contém:

* Distribuições de vendas por continente
* Gêneros mais lucrativos
* Editoras com maiores médias de vendas
* Evolução temporal das vendas
* Correlações entre atributos numéricos
* Comparações entre plataformas

Todas as visualizações encontram-se no notebook `01_eda.ipynb`.

---

## 5. Modelagem e Machine Learning

Após testar diferentes modelos, optou-se pelo **RandomForestRegressor**, devido ao melhor equilíbrio entre:

* estabilidade
* explicabilidade
* desempenho

O modelo foi treinado utilizando:

* Variáveis categóricas codificadas
* Padronização de vendas regionais
* Seleção de features relevantes

A métrica utilizada foi:

* RMSE (Root Mean Squared Error)
* R² Score

---

## 6. Resultados

O modelo final apresentou:

* **RMSE:** aproximadamente 0.43
* **R²:** aproximadamente 0.92

Interpretando:

* O erro médio do modelo é baixo em relação ao volume médio de vendas.
* O modelo explica cerca de 92% da variância das vendas globais.

---

## 7. Conclusão

O projeto demonstrou a aplicação dos conceitos de:

* manipulação e limpeza de dados
* criação de features
* análise exploratória
* modelagem regressiva
* avaliação de desempenho

### Principais aprendizados

* A escolha do modelo tem grande impacto em datasets com alta variabilidade.
* A limpeza e padronização dos dados é fundamental para bons resultados.
* A EDA é essencial para entender o comportamento do mercado e orientar o modelo.

### Limitações

* O dataset possui inconsistências históricas e valores faltantes.
* As vendas globais podem ser influenciadas por fatores não presentes no dataset (marketing, avaliação crítica, orçamento, etc.).

### Trabalhos futuros

* Testar modelos de Gradient Boosting (XGBoost, LightGBM).
* Criar previsões separadas por região.
* Desenvolver um dashboard interativo com Power BI ou Streamlit.

---
