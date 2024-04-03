## Objetivo:


Garantir a prioridade de operadores, garantir que é LL(1) e calcular look aheads.
```
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b / (a / b)
```


## Resolução:

```
Z -> Start '$' {'!',var,'?'}

Start -> '?' Exp {'?'}
    |  var '=' Exp {var}
    |  '!' Exp {'!'}


Exp -> Termo Exp2 {var, number, '('}

Exp2 -> '+' Exp {'+'}
    |  '-' Exp {'-'}
    |  & {'$', ')'}


Termo -> Fator Termo2 {var, number, '('}

Termo2 -> '*' Termo {'*'}
    |  '/' Termo {'/'}
    |  & {'$', ')'}


Fator -> '(' Exp ')' {'('}
    | number {number}
    | var {var}
```