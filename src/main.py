import pandas as pd
from etl.load import carregar_dados
from etl.clean import limpar_dados
from etl.transform import criar_features
from ml.preprocess import preparar_treino
from ml.train import treinar_modelo
from ml.evaluate import avaliar_modelo

print("Carregando dados...")
df = carregar_dados("data/raw/video_games_sales.csv")

print("Limpando dados...")
df = limpar_dados(df)

print("Criando features...")
df = criar_features(df)

print("Preparando dados para machine learning...")
X_train, X_test, y_train, y_test, preprocessor = preparar_treino(df)

print("Treinando modelo...")
modelo = treinar_modelo(preprocessor, X_train, y_train)

print("Avaliando modelo...")
resultados = avaliar_modelo(modelo, X_test, y_test)

print("-" * 60)
print("RESULTADOS DO NOVO MODELO:")
print(resultados)
print("-" * 60)
