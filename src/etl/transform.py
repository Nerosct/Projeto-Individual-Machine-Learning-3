import pandas as pd

def criar_features(df):
    # Remover variáveis proibidas (que causam fuga de informação)
    df = df.drop(columns=[
        "NA_Sales",
        "EU_Sales",
        "JP_Sales",
        "Other_Sales"
    ])

    # Transformar ano
    df["Year"] = df["Year"].fillna(df["Year"].median())

    # Criar bin de década
    df["Decade"] = (df["Year"] // 10) * 10

    return df
