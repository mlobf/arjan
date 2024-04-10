from base import produtos
from pprint import pprint
from functools import reduce

# Quando eu tenho que pegar somente uma coluna dentro de um objeto eu penso em list compreention.

precos = map(lambda p: p.get("preco"), produtos)


# Usando map()
# a variavel precos é um objeto do tipo iterador.
# print(list(precos)) #Retorna como uma lista
# pprint(list(produtos))

# print(next(precos)) # next é uma funcao propria de um objeto iterador
# Ela retorna sempre o proximo elemento contido dentro de um objeto iterador.
# pprint(list(precos))
# Uma vez que o objeto iterador é convertido em um novo tipo de elemento, por exemplo
# uma tupla ou lista, ele deixa de poder usar as funcoes dele, como por exemplo a next()
# print(next(precos))

# Usando list_coomprehensions
# usando_o_list = [round(produto.get("preco") * 1.01) for produto in produtos]

# Usando o Filter
# Quero fazer uma selecao de valores de acordo com um criterio.
# produtos_filter = list(filter(lambda p: p.get("preco") > 20, produtos))
# pprint(produtos_filter)
# Usando o map e o filter juntos
"""
produtos_map_filter = list(
    map(lambda p: p.get("preco"), list(filter(lambda p: p.get("preco") > 20, produtos)))
)
pprint(produtos_map_filter)
list_comprehension = [produto for produto in produtos if produto.get("preco") > 20]
pprint(list_comprehension)
"""

# Usando o Reduce
# Quero somar os preços
soma_valor_dos_produtos = round(reduce(lambda ac, p: ac + p.get("preco"), produtos, 0))
print(soma_valor_dos_produtos)
