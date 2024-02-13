# Análise de um dataset

## Objetivo

- Ler um dataset em formato `csv`.
- Manipular os dados através de um *script* python.
- Apresentar os dados no terminal.

## Método utilizado no *script*

### Leitura do dataset

O dataset é lido através do comando `cat` e dado por `stdin` ao *script* através do comando *pipe* (`|`).

### Manipulação de dados

O *script* percorre uma vez as linhas recebidas no `stdin` e armazena as informações necessárias.

As informações apresentadas foram calculadas da seguinte forma:
- As **modalidades** são guardadas numa lista, inserindo apenas elementos únicos (que ainda não se encontrem na lista) e ordenada antes da sua impressão no terminal
- A **percentagem de atletas aptos e inaptos** é calculada através do número total de atletas e do número de atletas aptos para a prática desportiva, sendo o número de atletas inaptos a diferença entre estes dois valores
- A **distribuição dos atletas por escalões** é calculada através do armazenamento do numero de atletas para cada idade num dicionário

## Notas finais

Para correr o programa é necessário utilizar o comando `cat emd.csv | python3 reader.py`.
