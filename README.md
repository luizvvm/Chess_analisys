# Analisador de Partidas de Xadrez com Python

Este projeto é um script em Python que utiliza as bibliotecas `python-chess`, `numpy` e a engine `stockfish` para realizar uma análise estatística de uma partida de xadrez a partir de um arquivo PGN, um projeto feito para estudos.

## Descrição

O objetivo principal deste repositório é aplicar e aprimorar minhas habilidades em Python para Ciência de Dados, explorando o xadrez.

O projeto começou com um script focado em extrair a avaliação em centipeões de cada lance de uma única partida (utilizando `python-chess` e `stockfish`). Agora, o escopo foi expandido para incluir uma análise exploratória de dados em um dataset com mais de 20.000 partidas, utilizando as bibliotecas `pandas` e `matplotlib`.

Este projeto foi desenvolvido como parte dos meus estudos em Python para Ciência de Dados, apenas quero testar algumas coisas da biblioteca NumPy, Pandas e também dar uma olhada em duas bibliotecas que tenho interesse em aprender mais sobre, que é a do chess e a do stockfish.

#### Módulo 1: Análise de Partida Individual (com Stockfish)
* Leitura de partidas de xadrez no formato PGN.
* Análise lance a lance utilizando a engine Stockfish para obter a avaliação da posição.
* Cálculo de estatísticas descritivas da partida:
    * Vantagem Média de cada jogador.
    * Volatilidade (Desvio Padrão) da partida.
    * Melhor e Pior Posição para as Brancas.
* Geração de um relatório de análise simples no console.

#### Módulo 2: Análise de Dataset (com Pandas)
* Carregamento e limpeza de um grande dataset de partidas (`.csv`).
* Análise de popularidade das aberturas mais jogadas.
* Cálculo das taxas de vitória, derrota e empate para diferentes aberturas.
* Estudo da correlação entre o rating dos jogadores e suas escolhas.
* Visualização de dados com `matplotlib` para apresentar os insights encontrados.

## Tecnologias Utilizadas

* **Python 3.x**
* **Pandas:**
* **NumPy:**
* **Matplotlib:**
* **python-chess:** 
* **stockfish:** 

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

O projeto é dividido em dois módulos de análise.

#### Para Análise de Partida Individual:
1.  Coloque um arquivo `.pgn` de sua escolha na pasta `data/`.
2.  No script `src/analise_partida_individual.py`, ajuste o nome do arquivo na linha `with open(...)` e o caminho para o executável do Stockfish.
3.  Execute o script:
    ```bash
    # Estando na pasta raiz do projeto
    python src/analise_partida_individual.py
    ```

#### Para Análise do Dataset:
1.  Certifique-se de que o arquivo `games.csv` está na pasta `data/`.
2.  Execute o script de análise exploratória:
    ```bash
    # Estando na pasta raiz do projeto
    python src/01_exploracao_inicial.py
    ```

## Melhorias Futuras

## Melhorias Futuras

* [ ] **Módulo 1:** Gerar um gráfico da avaliação ao longo da partida individual usando `matplotlib`.
* [ ] **Módulo 2:** Expandir a análise estatística do dataset, cruzando aberturas com as taxas de vitória e o rating dos jogadores.
* [ ] **Módulo 2:** Criar um dashboard interativo com `Plotly` ou `Streamlit` para explorar as estatísticas das aberturas.
* [ ] Criar uma interface gráfica simples com `Tkinter` ou `PySimpleGUI` para facilitar a análise de partidas individuais.

Talvez:
* [ ] Mostrar a precisão das partidas (isso é mais difícil do que parece, pois envolve conceitos mais avançados de Machine Learning e estatística)

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE.txt` para mais detalhes.