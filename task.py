import secrets
import string
import random

class GeneratePassword:
    def __init__(self,length_password):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        length_password = None

    def generate(self):
        try:
            length_password = int(self.length_password)
            if length_password < 8 or length_password > 32:
                print('Введите цифру от 8 до 32')
            else:
                password= ''.join(secrets.choice(self.alphabet) for i in range(self.length_password))
                print(f"length password: {self.length_password}, password: {password}")
        except:
            print('Введите цифру')

    def start(self):
        print('''
Добро пожаловать в генератор паролей!
Если захотите выйти из генератора паролей, введите "exit"
''')
        while True:
            self.length_password = input('''
Введите длину пароля (введите цифру от 8 до 32): ''')
            if self.length_password == 'exit':
                print('До свидания')
                break
            self.generate()
            
