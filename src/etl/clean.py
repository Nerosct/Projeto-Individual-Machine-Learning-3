import pandas as pd

def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Remover linhas 100% nulas
    df.dropna(how="all", inplace=True)

    # Preenchimentos simples
    df["Publisher"].fillna("Unknown", inplace=True)
    df["Year"].fillna(df["Year"].median(), inplace=True)

    # Converter tipos
    df["Year"] = df["Year"].astype(int)

    # Remover valores negativos
    colunas_vendas = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
    for coluna in colunas_vendas:
        df = df[df[coluna] >= 0]

    return df
