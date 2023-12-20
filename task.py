import secrets
import string
import random
import sys

class GeneratePassword:
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + string.punctuation
        self.length_password = 8

    def generate(self):
        try:
            self.length_password = int(self.length_password)
            if self.length_password < 8 or self.length_password > 32:
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
        print(sys.argv)
        if len(sys.argv) > 1:
            self.length_password = sys.argv[1]
            self.generate()
        else:
            print("Длина пароля не указана")
                

gen_pas = GeneratePassword()
gen_pas.start()
            
