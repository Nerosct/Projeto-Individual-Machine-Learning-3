import matplotlib.pyplot as plt
import seaborn as sns

def vendas_por_genero(df):
    plt.figure(figsize=(10,4))
    df.groupby("Genre")["Global_Sales"].sum().sort_values().plot(kind="bar")
    plt.title("Vendas Globais por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Vendas (milhões)")
    plt.tight_layout()
    plt.show()

def vendas_por_plataforma(df):
    top = df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False).head(15)
    plt.figure(figsize=(10,4))
    top.plot(kind="bar")
    plt.title("Top 15 Plataformas por Vendas Globais")
    plt.xlabel("Plataforma")
    plt.ylabel("Vendas (milhões)")
    plt.tight_layout()
    plt.show()

def calor_correlacao(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="Blues")
    plt.title("Matriz de Correlação")
    plt.show()
