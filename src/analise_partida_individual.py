# src/analise_partida_individual.py

import chess.pgn
import numpy as np
import pandas as pd
import plotly.express as px
from stockfish import Stockfish

def analisar_partida(caminho_pgn, caminho_stockfish):
    try:
        # Inicializando a engine do Stockfish
        stockfish = Stockfish(path=caminho_stockfish)
        #Mexa no hash abaixo para deixar o stockfish mais potente. Se eu não me engano está relacionada a quanta RAM vc vai estar disponibilizando
        stockfish.update_engine_parameters({"Hash": 8192})

        # Carregando o pgn da partida
        with open(caminho_pgn) as pgn:
            primeiro_jogo = chess.pgn.read_game(pgn)

        nome_brancas = primeiro_jogo.headers.get("White", "Brancas")
        nome_pretas = primeiro_jogo.headers.get("Black", "Pretas")

        tabuleiro = chess.Board()
        lista_lances_temporario = []
        num_lances = 0

        # Percorre cada lance da linha principal da partida
        for lance in primeiro_jogo.mainline_moves():
            num_lances += 1
            tabuleiro.push(lance)
            stockfish.set_fen_position(tabuleiro.fen())
            avaliacao = stockfish.get_evaluation()["value"]
            lista_lances_temporario.append([num_lances, avaliacao])

        # Passando a lista para array numpy
        lista_lances = np.array(lista_lances_temporario)

        # Cálculando as Estatísticas
        status = {"media": np.mean(lista_lances[:, 1]), "volatilidade": np.std(lista_lances[:, 1]), "melhor_posicao": np.max(lista_lances[:, 1]), "pior_posicao": np.min(lista_lances[:, 1])
        }

        #Criando o Gráfico com Plotly
        df_partida = pd.DataFrame(lista_lances, columns=['Lance', 'Avaliacao_CP'])
        
        fig = px.line(df_partida, x='Lance', y='Avaliacao_CP', title=f'Avaliação da Partida: {nome_brancas} vs {nome_pretas}', labels={'Lance': 'Número do Lance', 'Avaliacao_CP': 'Avaliação (Centipeões)'}, markers=True)
        fig.add_hline(y=0, line_dash="dash", line_color="gray")
        
        return fig, status
    
    except Exception as e:
        print(f"Erro ao analisar a partida: {e}")
        return None, None

# O bloco abaixo só será executado se você rodar este script diretamente. Aprendi isso aqui: https://youtu.be/KZpYtNtGxSU?si=05429KVsxutHoYbU.
# Ele é necessário para exitar que o Streamlit execute ele ao importar a função acima.
if __name__ == '__main__':
    caminho_pgn_teste = '../data/chess_game_1.pgn'
    caminho_stockfish_teste = "D:/stockfish/stockfish/stockfish-windows-x86-64-avx2.exe"
    
    figura_resultado, estatisticas_resultado = analisar_partida(caminho_pgn_teste, caminho_stockfish_teste)

    print("- Estatísticas da partida -")
    for chave, valor in estatisticas_resultado.items():
        print(f"{chave.capitalize()}: {valor:.2f}")

    print("Exibindo o gráfico interativo...")
    figura_resultado.show()
