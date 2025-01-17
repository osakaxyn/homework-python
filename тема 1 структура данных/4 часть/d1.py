"""
Поработайте с каждым методом списка,
особенно pop, insert и extend.
напишите по одной функции для каждого из них хотя бы.
"""

bloodybreezy = ['jogu', 'dzhmyrzik', 'olkash']

def teso(bloodybreezy):
    reranteso = bloodybreezy.pop(2)
    print(bloodybreezy)

teso(bloodybreezy)

bloodybreezy1 = ['jogu', 'dzhmyrzik', 'olkash']

def noteso(bloodybreezy1):
    rerannoteso = bloodybreezy1.insert(1, 'SHYRH')
    print(bloodybreezy1)

noteso(bloodybreezy1)


bloodybreezy2 = ['jogu', 'dzhmyrzik', 'olkash']

def chuvaki(bloodybreezy2):
    more_chuvaki = ['BISH', 'VAIPA']
    bloodybreezy2.extend(more_chuvaki)
    print(bloodybreezy2)

chuvaki(bloodybreezy2)
