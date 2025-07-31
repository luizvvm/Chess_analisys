# Chess Analysis Dashboard

Uma aplicação web interativa para análise e visualização de dados de partidas de xadrez, construída com Python, Streamlit e PostgreSQL.

## Sobre o Projeto

Desenvolvi essa aplicação web apenas para fins didáticos. O objetivo é estudar NumPy, Pandas, Postgre, streamlit, Plotly e muito mais, conforme eu for aprendendo. Sendo assim, atualmente esse projeto é uma plataforma para analisar tanto partidas de xadrez individuais quanto um grande volume de jogos, mas isso pode mudar conforme eu for tendo ideias ou conforme eu for estudando outras tecnologias.

Sobre a aplicação, ela se conecta a um banco de dados PostgreSQL, que armazena um dataset com mais de 20.000 partidas (link pro data set: https://www.kaggle.com/datasets/datasnaek/chess), permitindo análises estatísticas sobre aberturas e performances dos jogadores.

### Funcionalidades Principais

* *Dashboard Interativo:* Interface web desenvolvida com Streamlit, permitindo a navegação entre diferentes módulos de análise.
* *Análise de Partida Individual:* Permite o upload de um arquivo PGN para uma análise detalhada lance a lance, utilizando a engine Stockfish para obter a avaliação de cada posição da sua partida.
* *Visualização Dinâmica:* Gráficos interativos gerados com Plotly que exibem a vantagem em centipeões ao longo da partida.
* *Estatísticas do Dataset:* Análise de um grande conjunto de dados para explorar a popularidade e as taxas de vitória das aberturas de xadrez mais comuns (pelo menos do Lichess).
* *Backend com Banco de Dados:* Utilização do PostgreSQL como sistema de gerenciamento de banco de dados para armazenar e consultar os dados das partidas de forma eficiente.

## Tecnologias Utilizadas

| Categoria                | Tecnologia                                           |
| ------------------------ | ---------------------------------------------------- |
| *Linguagem* | Python 3                                             |
| *Backend* | PostgreSQL, SQLAlchemy                               |
| *Frontend de Dados* | Streamlit, Plotly                                    |
| *Análise de Dados* | Pandas, NumPy                                        |
| *Motor de Xadrez* | python-chess, stockfish                          |
| *Ferramentas* | Git, GitHub, Ambientes Virtuais (venv)             |

## Instalação e Execução

Para executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

* Python 3.8 ou superior
* Git
* PostgreSQL instalado e em execução na máquina.
* Executável da engine Stockfish.

### 1. Configuração do Ambiente

Primeiro, clone o repositório e configure o ambiente virtual Python.

```bash
# Clone o repositório
git clone [https://github.com/luizvvm/Chess_analisys.git](https://github.com/luizvvm/Chess_analisys.git)
cd Chess_analisys

# Crie e ative o ambiente virtual
# No Windows:
python -m venv venv
.\venv\Scripts\activate

# Instale as dependências do projeto
pip install -r requirements.txt
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

### 5. Configuração do Banco de Dados

A aplicação utiliza um banco de dados PostgreSQL para armazenar os dados das partidas.

1.  **Crie o Banco de Dados:** Crie um novo banco de dados chamado `chess_db`.
2.  **Configure a Senha:** Abra o arquivo `src/ingest_data.py` e modifique a variável `db_password_raw` com a senha do seu usuário.
3.  **Popule o Banco de Dados:** Execute o script de ingestão de dados. Este comando precisa ser executado apenas uma vez, mas também não vai dar problema se você executar outra vez sem querer.
    ```bash
    # Estando na pasta raiz do projeto, com o venv ativo
    python src/ingest_data.py
    ```

### 6. Execução da Aplicação

1.  **Configure os Caminhos:** Abra o arquivo `app.py` e ajuste a variável `caminho_stockfish` aqui também. Ajuste também a senha do banco de dados neste arquivo.
2.  **Inicie o Dashboard:** Com o venv ainda ativo, execute o seguinte comando:
    ```bash
    streamlit run app.py
    ```
A aplicação será aberta automaticamente no seu navegador.

## Melhorias Futuras

* [ ] Mostrar a precisão das partidas (isso é mais difícil do que parece, pois envolve conceitos mais avançados de Machine Learning e estatística)
      
Pensarei em mais coisas conforme eu for estudando.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE.txt` para mais detalhes.
