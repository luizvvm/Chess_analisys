# src/Lichess_games_statistics.py

import pandas as pd
import plotly.express as px

def carregar_dados(caminho_csv, separador=','):
    try:
        df = pd.read_csv(caminho_csv, sep=separador)
        print("Dados carregados")
        return df
    except FileNotFoundError:
        print("Não achou o arquivo")
        return None

#top_n são as aberturas mais populares
def gerar_grafico_popularidade_aberturas(df, top_n=15):
    contagem_aberturas = df['opening_name'].value_counts().head(top_n)
    
    fig = px.bar(contagem_aberturas, x=contagem_aberturas.index, y=contagem_aberturas.values, title=f"Top {top_n} Aberturas Mais Jogadas", labels={'index': 'Abertura', 'y': 'Número de Partidas'})
    return fig

# O bloco abaixo só será executado se você rodar este script diretamente. Aprendi isso aqui: https://youtu.be/KZpYtNtGxSU?si=05429KVsxutHoYbU.
# Ele é necessário para exitar que o Streamlit execute ele ao importar a função acima.
if __name__ == '__main__':
    #apenas para testes locais
    caminho_csv_teste = '../data/games.csv'

    dataframe_jogos = carregar_dados(caminho_csv_teste)

    # 2. Se os dados foram carregados, gera e mostra o gráfico
    if dataframe_jogos is not None:
        print("Informações:")
        print(dataframe_jogos.info())
        
        figura_aberturas = gerar_grafico_popularidade_aberturas(dataframe_jogos)

        figura_aberturas.show()