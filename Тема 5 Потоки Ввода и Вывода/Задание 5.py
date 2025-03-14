"""
осмотрите видео про контекстный менеджер
и повторите все действия из видео с файлом из пункта 2
"""

# file = open('lorum.txt', 'w')
# file.write([1, 2, 3])
# file.close()

# lst = []
# for i in range(10000):
#     with open('lorum.txt', 'w') as f:
#         lst.append(f)
    # file.close()

# with print('lorum.txt', 'w') as f:
#     f.write('123')
#     f.write('hello')
# print(f.write('123'))

# import os
#
# with os.scandir(".") as entries:
#     for entry in entries:
#         print(entry.name , "->", entry.stat().st_size, "bytes")


# import  threading
#
#
# balance_lock = threading.Lock()
#
#
# # balance_lock.acquire()
# # balance_lock.release()
#
#
# # Через with
# with balance_lock:
#     pass # Делаем обработку



import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.run(main())  # Запускаем асинхронную функцию правильно


# import aiohttp
# print(aiohttp.__version__)  # Должен вывести номер версии
