# Analisador de Partidas de Xadrez com Python

Este projeto é um script em Python que utiliza as bibliotecas `python-chess`, `numpy` e a engine `stockfish` para realizar uma análise estatística de uma partida de xadrez a partir de um arquivo PGN, um projeto feito para estudos.

## Descrição

O objetivo principal deste script é extrair a avaliação em centipeões de cada lance de uma partida, armazenar esses dados e calcular métricas-chave como a vantagem média de cada jogador, a volatilidade do jogo e os picos de vantagem.

Este projeto foi desenvolvido como parte dos meus estudos em Python para Ciência de Dados, apenas queria testar algumas coisas da biblioteca NumPy e também dar uma olhada em duas bibliotecas que tenho interesse em aprender mais sobre, que é a do chess e a do stockfish.

## Funcionalidades Principais

* Leitura de partidas de xadrez no formato PGN.
* Análise lance a lance utilizando a engine Stockfish para obter a avaliações da posição em centipeões.
* Armazenamento e manipulação dos dados de avaliação com a biblioteca NumPy.
* Cálculo de estatísticas descritivas da partida (utilizando a biblioteca NumPy):
    * Vantagem Média
    * Volatilidade (Desvio Padrão)
    * Melhor e Pior Posição (do ponto de vista das Brancas)
* Geração de um relatório de análise simples no console.

## Tecnologias Utilizadas

* **Python 3.x**
* **NumPy:** Para manipulação de arrays e cálculos estatísticos.
* **python-chess:** Para leitura de arquivos PGN e manipulação do tabuleiro.
* **stockfish:** Como interface para a engine de xadrez Stockfish.

## Instalação e Configuração

Para rodar este projeto em sua máquina local, siga os passos abaixo:

**1. Clone o Repositório:**
```bash
git clone https://github.com/luizvvm/Chess_analisys
cd Chess_analisys
```
##2. Criar um ambiente virtual
Recomendavel para evitar qualquer erro por conflitos de bibliotecas.
```
# No Windows
python -m venv venv
.\venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
##3. Instalar os requerimentos
Com o ambiente virtual ativado, instale os pacotes necessários:
```execute
pip install -r requirements.txt
```

**3. Baixe a Engine Stockfish:**
Este script requer o **executável** da engine Stockfish.
* Faça o download no site oficial: [stockfishchess.org](https://stockfishchess.org/download/)
* Descompacte o arquivo `.zip`.

##4. Modificar o path
Modifique no código a linha:
```
stockfish = Stockfish(path="D:\\stockfish\\stockfish\\stockfish-windows-x86-64-avx2.exe")
```
para o diretório onde você baixou a engine.

## Como Usar

1.  Coloque o arquivo da partida que você deseja analisar na pasta raiz do projeto. O arquivo deve estar no formato PGN e nomeado assim: "chess_game_1.pgn".
2.  Certifique-se de que o nome do arquivo no script (na linha `with open(...)`) corresponde ao nome do seu arquivo PGN, por isso recomendo nomear como "chess_game_1.pgn".
3.  Execute o script através do terminal:
```bash
python xadrez_analises.py
```

## Melhorias Futuras

* [ ] Gerar um gráfico da avaliação ao longo da partida usando `matplotlib` quando eu aprender sobre ela.
* [ ] Criar uma interface gráfica simples com `Tkinter` ou `PySimpleGUI`.
* [ ] Criar um banco de partidas.
* [ ] Com base no banco de dados, criar um bot daquele jogador.

Talvez:
* [ ] Mostrar a precisão das partidas (isso é mais difícil do que parece, pois envolve conceitos mais avançados de Machine Learning e estatística)

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE.txt` para mais detalhes.