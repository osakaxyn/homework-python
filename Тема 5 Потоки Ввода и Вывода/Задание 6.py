"""
Прочитайте статью и выполните действия, которые там указаны с файлом bikes.csv
"""
# Подключаем библиотеку Pandas
import pandas as pd

# подключаем модуль pathlib и библиотеку Path модуля pathlib
import pathlib
from pathlib import Path

# Получаем строку, содержащую путь к рабочей директории:
work_path = pathlib.Path.cwd()

# сохраним путь к csv файлу в переменной data_path
data_path = Path(work_path, 'datasets', 'ks-projects-201801.csv')

# Загружаем данные из csv файла в переменную data
data = pd.read_csv(data_path, sep="|")

# Выведем первые 10 строк из прочитанного файла на экран
print(data.head(10))