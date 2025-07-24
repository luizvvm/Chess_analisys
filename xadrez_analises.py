import chess.pgn
from stockfish import Stockfish

#Carrega o stockfish.
stockfish = Stockfish(path="D:\\stockfish\\stockfish\\stockfish-windows-x86-64-avx2.exe")
stockfish.update_engine_parameters({"Hash": 4096})


#Carrega o pgn da partida
with open("chess_game_1.pgn") as pgn:
    primeiro_jogo = chess.pgn.read_game(pgn)

#Salva o nome dos jogadores
nome_brancas = primeiro_jogo.headers["White"]
nome_pretas = primeiro_jogo.headers["Black"]

#usando a biblioteca do chess para criar um tabuleiro
tabuleiro = chess.Board()

#Lista para guardar os lances
lista_lances = []

for lance in primeiro_jogo.mainline_moves():
    tabuleiro.push(lance)
    stockfish.set_fen_position(tabuleiro.fen())
    print(lance)
    print(stockfish.get_evaluation())

