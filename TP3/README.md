# Somador on/off

## Objetivo:

O objetivo do trabalho era criar em Python um pequeno programa que fizesse o seginte:

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caractere “=”, o resultado da soma é colocado na saída.

## Resolução:

Para resolver o problema, decidi utilizar a biblioteca `re` do Python para poder utilizar expressões regulares. Com essa biblioteca decidi utilizar o método `findall` para encontrar todas as ocorrências de uma determinada expressão regular no ficheiro que é dado como input.

A expressão regular utilizada foi `r'(on|off|=|-?[0-9]+)'`, visto que encontra no texto todas as ocorrências de **on**, **off*, **=** assim como **sequências de dígitos** podendo ser eles negativos ou positivos, com ou sem sinal.

Com o findall dei assim parse a todos esses comandos possíveis, aparecendo de forma cronológica de acordo com o texto, numa lista.

Para cada comando na lista, é executada a operação ou adicionado o valor caso não seja uma operação.


**Para correr o programa:** 

```python3 code.py file.txt```