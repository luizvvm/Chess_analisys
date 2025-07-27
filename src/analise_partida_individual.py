import chess.pgn
import numpy as np
import pandas as pd
import plotly.express as px
from stockfish import Stockfish

#Carrega o stockfish.
stockfish = Stockfish(path="D:/stockfish/stockfish/stockfish-windows-x86-64-avx2.exe")
stockfish.update_engine_parameters({"Hash": 4096})


#Carrega o pgn da partida
with open("../data/chess_game_1.pgn") as pgn:
    primeiro_jogo = chess.pgn.read_game(pgn)

#Salva o nome dos jogadores
nome_brancas = primeiro_jogo.headers["White"]
nome_pretas = primeiro_jogo.headers["Black"]

#usando a biblioteca do chess para criar um tabuleiro
tabuleiro = chess.Board()

#Lista para guardar os lances
lista_lances_temporario = []

num_lances = 0

#for que percorre cada lance da linha principal do jogo
for lance in primeiro_jogo.mainline_moves():
    num_lances += 1
    #coloca cada lance no tabuleiro
    tabuleiro.push(lance)
    #entrega o tabuleiro (com a posição atual) pro stockfish
    stockfish.set_fen_position(tabuleiro.fen())
    lista_lances_temporario.append( [num_lances, (stockfish.get_evaluation())["value"]])

#passando a lista para array numpy
lista_lances = np.array(lista_lances_temporario)

#aplicando oque eu aprendi sobre a biblioteca numpy
avaliacao_media = np.mean(lista_lances[:, 1])
volatibilidade = np.std(lista_lances[:, 1])

#sempre do ponto de vista das brancas
melhor_posicao = np.max(lista_lances[:, 1])
pior_posicao = np.min(lista_lances[:, 1])

# dataframe para visualização
df_partida = pd.DataFrame(lista_lances, columns=['Lance', 'Avaliacao_CP'])

#Criando o gráfico
fig = px.line(df_partida, x='Lance', y='Avaliacao_CP', title=f'Avaliação da Partida: {nome_brancas} vs {nome_pretas}', labels={'Lance': 'Número do Lance', 'Avaliacao_CP': 'Avaliação (Centipeões)'}, markers=True
)

#Linha apenas para referência
fig.add_hline(y=0, line_dash="dash", line_color="gray")
fig.show()

print(f"Avaliação Média: {avaliacao_media:.2f}")
print(f"Volatilidade: {volatibilidade:.2f}")
print(f"Melhor Posição (Brancas): {melhor_posicao}")
print(f"Pior Posição (Brancas): {pior_posicao}")
