"""
Попробуйте открыть файлы с разными значениями mode для чтения.
"""

file = open('lorum.txt', "a+", encoding='utf-8')
file.seek(0)
print(file.read())