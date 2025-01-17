"""
Преобразуйте список [«a», «s», «1», «a», «32», «23»] в set и выведите на экран.
Что изменилось?
"""

sas = ["a", "s", "1", "a", "32", "23"]

def defa(sas):
    sas_set = set(sas)
    print(*sas_set)

defa(sas)