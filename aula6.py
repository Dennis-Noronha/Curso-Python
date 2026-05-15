# Conversão de tipos, coerção. 
# type conversion, type casting, coercion
""" O Python é uma linguagem de tipagem dinâmica,
    o que significa que as variáveis podem mudar de tipo durante a execução do programa. 
    No entanto, às vezes é necessário converter um """

# Tipo imutaveis e primitivos: string, int, float, bool
# Tipo mutáveis: list, dict, set 
print ( 1 + 1 ) # O resultado é 2, que é do tipo int
print('a' + 'b') # O resultado é 'ab', que é do tipo str
print(1 + 1.0) # O resultado é 2.0, que é do tipo float
print(1 + True) # O resultado é 2, pois True é convertido para 1, e False seria convertido para 0
print('5' + '5') # O resultado é '55', pois ambos os operandos são strings, e a operação de adição é concatenada
print(int('5') + int('5')) # O resultado é 10, pois as strings '5' são convertidas para inteiros antes da adição
print(float('3.14') + float('2.71')) # O resultado é 5.85, pois as strings '3.14' e '2.71' são convertidas para floats antes da adição 