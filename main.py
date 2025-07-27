import streamlit as st
import pandas as pd
import plotly.express as px

from src.analise_partida_individual import analisar_partida
from src.Lichess_games_statistics import carregar_dados, gerar_grafico_popularidade_aberturas

st.set_page_config(layout="wide")
st.title("Dashboard de Análises de Xadrez")

# Barra de navegação lateral
st.sidebar.title("Navegação")
pagina = st.sidebar.selectbox("Escolha uma análise", ["Análise de Partida Individual", "Estatísticas de Aberturas"])

###########################################################################
#Página 1
if pagina == "Análise de Partida Individual":
    st.header("Análise de Partida Individual com Stockfish")

    caminho_stockfish = st.text_input("Cole o caminho para o executável do Stockfish do seu pc", "D:/stockfish/stockfish/stockfish-windows-x86-64-avx2.exe"
    )

    arquivo_carregado = st.file_uploader("Escolha um arquivo PGN", type="pgn")
    
    if arquivo_carregado is not None:
        # Botão para o usuário confirmar
        if st.button("Analisar Partida"):
            #Esse spinner é utilizado para mostrar a mensagem "carregando"
            with st.spinner("Analisando..."):
                
                # Salva o arquivo enviado em um local temporário para a função poder ler
                with open("temp_game.pgn", "wb") as f:
                    f.write(arquivo_carregado.getbuffer())

                fig_partida, status = analisar_partida("temp_game.pgn", caminho_stockfish)

                #exibindo os resultados
                if fig_partida and status:
                    st.success("Análise concluída com sucesso!")
                    
                    st.plotly_chart(fig_partida, use_container_width=True)

                    st.subheader("Estatísticas da Partida")
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Avaliação Média", f"{status['media']:.0f}")
                    col2.metric("Volatilidade", f"{status['volatilidade']:.0f}")
                    col3.metric("Melhor Posição (Brancas)", f"{status['melhor_posicao']:.0f}")
                    col4.metric("Pior Posição (Brancas)", f"{status['pior_posicao']:.0f}")


###########################################################################
#Página 2
elif pagina == "Estatísticas de Aberturas":
    st.header("Análise do Dataset de Partidas")

    df = carregar_dados("data/games.csv", separador=',')

    if df is not None:
        st.dataframe(df.head())

        # Gráfico de popularidade de aberturas
        st.subheader("Popularidade das Aberturas")
        fig_aberturas = gerar_grafico_popularidade_aberturas(df)

        if fig_aberturas:
            st.plotly_chart(fig_aberturas, use_container_width=True)