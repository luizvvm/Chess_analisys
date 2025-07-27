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
    from sqlalchemy import create_engine
    #precisamos dessa biblioteca aqui porque eu tive que encriptografar a senha
    from urllib.parse import quote_plus

    db_password_raw = "Postgre_vitor_vep07@" 
    db_password_encoded = quote_plus(db_password_raw)
    db_nome = "chess_db"
    db_usuario = "postgres"
    db_host = "127.0.0.1"
    db_port = "5432"
    DATABASE_URL = f"postgresql://{db_usuario}:{db_password_encoded}@{db_host}:{db_port}/{db_nome}"

    # O @st.cache_data serve para não rodar a consulta ao banco de dados toda vez que o usuario mexe em um filtro
    @st.cache_data
    def carregar_dados_do_banco():
        try:
            engine = create_engine(DATABASE_URL)
            # Executando uma consulta SQL para selecionar todos os dados da tabela "games"
            df = pd.read_sql("SELECT * FROM games", engine)
            return df
        except Exception as e:
            st.error(f"Erro ao conectar com o banco de dados: {e}")
            return None

    st.header("Análise do Dataset de Partidas (PostgreSQL)")

    #carregando os dados do banco
    df = carregar_dados_do_banco()

    # Só continua se os dados foram carregados com sucesso
    if df is not None:
        st.dataframe(df.head())
        st.subheader("Popularidade das Aberturas")
        
        # Usa a mesma função de antes para gerar o gráfico
        fig_aberturas = gerar_grafico_popularidade_aberturas(df)

        if fig_aberturas:
            st.plotly_chart(fig_aberturas, use_container_width=True)