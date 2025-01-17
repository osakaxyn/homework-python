"""
Дан список [«a», «s», «1», «a», «32», «23»].
Разбейте его на два списка: только с буквами и только с числами.
"""


spisok = ["a", "s", "1", "a", "32", "23"]

def araara(spisok):
    print(spisok[0], spisok[1], spisok[3])
    print(spisok[2], *spisok[4 : 6])

araara(spisok)

