import random
import string
import time
from cryptography.fernet import Fernet
from alive_progress import alive_bar


class PasswordGenerator:
    def __init__(self, length, count):
        self.length = length
        self.count = count

    def generate_passwords(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        passwords = []
        for _ in range(self.count):
            password = ''.join(random.choice(characters) for _ in range(self.length))
            passwords.append(password)
        return passwords


class PasswordManager:
    def __init__(self):
        self.generator = PasswordGenerator(12, 10)  # Параметры генерации паролей по умолчанию

    def set_password_generator(self, length, count):
        self.generator = PasswordGenerator(length, count)

    def input_password_length(self):
        while True:
            try:
                length = int(input('Введите желаемую длину пароля: '))
                if length <= 0:
                    print('Длина пароля должна быть положительным числом!')
                else:
                    return length
            except ValueError:
                print('Неверный формат данных! Введите целое число.')

    def input_password_count(self):
        while True:
            try:
                count = int(input('Введите нужное количество паролей: '))
                if count <= 0:
                    print('Количество паролей должно быть положительным числом!')
                else:
                    return count
            except ValueError:
                print('Неверный формат данных! Введите целое число.')

    def generate_passwords(self):
        length = self.input_password_length()
        count = self.input_password_count()
        self.set_password_generator(length, count)
        passwords = self.generator.generate_passwords()
        return passwords


class FileManager:
    @staticmethod
    def write_passwords_to_file(passwords):
        timestamp = time.strftime('%Y%m%d-%H%M%S')
        file_name = f'passwords_{timestamp}.txt'
        with open(file_name, 'w') as file:
            for password in passwords:
                file.write(password + '\n')
        print('Пароли сохранены в файле:', file_name)

    @staticmethod
    def generate_encryption_key():
        key = Fernet.generate_key()
        with open('encryption.key', 'wb') as key_file:
            key_file.write(key)
        print('Сгенерирован ключ шифрования.')

    @staticmethod
    def load_encryption_key():
        try:
            with open('encryption.key', 'rb') as key_file:
                key = key_file.read()
            return key
        except FileNotFoundError:
            print('Файл ключа шифрования не найден.')
            return None

    @staticmethod
    def encrypt_file(key, filename):
        if key is None:
            print('Отсутствует ключ шифрования. Сначала сгенерируйте ключ.')
            return
        f = Fernet(key)
        with open(filename, 'rb') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)
        print('Файл успешно зашифрован.')

    @staticmethod
    def decrypt_file(key, filename):
        if key is None:
            print('Отсутствует ключ шифрования. Сначала сгенерируйте ключ.')
            return
        f = Fernet(key)
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
        with open(filename, 'wb') as file:
            file.write(decrypted_data)
        print('Файл успешно расшифрован.')


class PasswordManagerApp:
    def __init__(self):
        self.password_manager = PasswordManager()
        self.file_manager = FileManager()

    @staticmethod
    def display_passwords(passwords):
        for password in passwords:
            print(password)

    def run(self):
        print('Добро пожаловать в Password Manager!')
        print('Это приложение позволяет генерировать пароли и шифровать/расшифровывать файлы.')
        while True:
            print('Меню:')
            print('1: Генерация паролей')
            print('2: Зашифровать файл')
            print('3: Расшифровать файл')
            print('0: Выход')

            choice = input('Ваш выбор: ')
            if choice == '1':
                passwords = self.password_manager.generate_passwords()
                print('Сгенерированные пароли:')
                self.display_passwords(passwords)
                self.file_manager.write_passwords_to_file(passwords)
            elif choice == '2':
                filename = input('Введите имя файла для шифрования: ')
                self.file_manager.generate_encryption_key()
                key = self.file_manager.load_encryption_key()
                self.file_manager.encrypt_file(key, filename)
                print('Файл успешно зашифрован.')
            elif choice == '3':
                filename = input('Введите имя файла для расшифровки: ')
                key = self.file_manager.load_encryption_key()
                self.file_manager.decrypt_file(key, filename)
                print('Файл успешно расшифрован.')
            elif choice == '0':
                print('До свидания!')
                break
            else:
                print('Неверный выбор. Пожалуйста, выберите существующую опцию.')


if __name__ == '__main__':
    app = PasswordManagerApp()
    app.run()
