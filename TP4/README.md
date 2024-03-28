# Analisador Léxico

## Objetivo:

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
`Select id, nome, salario From empregados Where salario >= 820`


## Resolução:

As expressões usadas têm em consideração a particularidade de que expressões como o `Select` podem aparecer também como `SELECT`.

De seguida, apenas separei as expressões de sinais de maior, menor ou igual e também separei os valores que as chaves possuiam.


**Para correr o programa:** 

```python3 code.py```
