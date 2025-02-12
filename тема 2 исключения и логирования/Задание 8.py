"""
Посмотрите видео и повторите код,
с помощью которого реализуются собственные исключения.
Постарайтесь разобраться в данном коде.
"""


class PrintData:
    def print(self, data):
        self. send_data (data)
        print(f'печать: {str(data)}')


    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception ("принтер не отвечает")

    def send_to_print (self, data):
        return True


p = PrintData()
try:
    p.print ("123")
except Exception:
    print ("принтер не отвечает")