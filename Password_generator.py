import random
import time
from cryptography.fernet import Fernet


def input_len():
    len_pass = 0

    while len_pass <= 0:
        try:
            len_pass = int(input('ВВЕДИТЕ ЖЕЛАЕМУЮ ДЛИНУ ПАРОЛЯ  \nВВЕДИТЕ ЧИСЛО>>>>  '))
        except Exception as err:
            print(err)
            print('!!!____Введен НЕВЕРНЫЙ формат данных,введите ЧИСЛО___!!!')
    return len_pass


def input_count():
    count = 0
    while count <= 0:
        try:
            count = int(input('ВВЕДИТЕ НУЖНОЕ КОЛИЧЕСТВО ПАРОЛЕЙ>>>>   '))
        except Exception as err:
            print(err)
            print('!!!____Введен НЕВЕРНЫЙ формат данных,введите ЧИСЛО___!!!')
    return count


def create_password(count, lenpass):
    test = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()')
    i = 0
    password = ''
    password_list = list()
    while i <= count - 1:
        for x in range(lenpass):
            password += random.choice(test)
        password_list.append(password)
        password = ''
        i += 1
    return password_list


def ask_write_to_file(passwords):
    p_count = time.ctime()
    file_name = p_count.strip(' ') + '.txt'
    for p in passwords:
        with open(file_name, 'a') as file:
            file.writelines(p + ' \n')
    print('ПАРОЛИ СГЕНЕРИРОВАНЫ!!!')
    time.sleep(1.5)
    return file_name


def no_write(passwords):
    str_count = 0
    for p in passwords:
        str_count += 1
        print(f'Ваш {str_count}-й пароль : {p}')


def ask_crypt(filename):
    generate_key = input('У Вас есть ключ шифрования? "y" or "n"')
    while generate_key.lower() != 'n' and generate_key.lower() != 'y':
        generate_key = input('!!!___ВВЕДИТЕ "Y" ИЛИ "N" ')
    _ = '.'
    if generate_key == 'n':
        for i in range(5):
            time.sleep(2)
            print(f'Ключ создается{_ * i}')
        wirte_key()
        print("Ключ создан")
        encrypt(load_key(), filename)
        print('файл зашифрован!')
    else:
        while True:
            input_path = input(r'введите путь до ключа')
            try:
                encrypt(path_to_key(input_path), filename)
                for i in range(5):
                    time.sleep(2)
                    print('Процесс шифрования', _ * i)
                print('файл зашифрован!')
                break
            except:
                print('Извините ваш ключ не подходит,либо не найден!!!')


def decrypt_file(filename, path):
    _ = '.'
    try:
        open(path, 'rb').read()
        for i in range(5):
            time.sleep(2)
            print('Процесс расшифровки', _ * i)
        decrypt(filename, path)
        print("Файл расшифрован!")
    except:
        print('Извините ключ не найден!')


def wirte_key():
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)


def path_to_key(path):
    return open(path, 'rb').read()


def load_key():
    return open('crypto.key', 'rb').read()


def encrypt(key, filename):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


def load_key_decrypt():
    key = input('введите путь к ключу')
    return open(key, 'rb').read()


if __name__ == '__main__':
    def main():
        hello = input('''ПРИВЕТ , ЭТА ПРОГРАММА ПОМОЖЕТ ТЕБЕ СГЕНЕРИРОВАТЬ НАДЕЖНЫЕ ПАРОЛИ
         ПО ТВОИМ ПРЕДПОЧТЕНИЯМ,ТАКЖЕ ИХ БУДЕТ ВОЗМОЖНО ЗАШИФРОВАТЬ В ФАЙЛ,ПОСЛЕ ИХ МОЖНО РАСШИФРОВАТЬ.
         ВЫБЕРИТЕ НУЖНЫЙ ВАМ РЕЖИМ:
         --- 1: СГЕНЕРИРОВАТЬ ПАРОЛИ И ПРОСТО ВЫВЕСТИ ИХ НА ЭКРАН ---
         --- 2: СГНЕНЕРИРОВАТЬ ПАРОЛИ И ЗАПИСАТЬ В ФАЙЛ ---
         --- 3: СГНЕНЕРИРОВАТЬ ПАРОЛИ И ЗАПИСАТЬ В ФАЙЛ, ПОСЛЕ ЗАШИФРОВАТЬ---
         --- 4: РАСШИФРОВАТЬ ФАЙЛ ---
         ВВЕДИТЕ НОМЕР: ....''')
        if hello == '1':
            len_password = input_len()
            count = input_count()
            get_list_password = create_password(count, len_password)
            ask_write = no_write(get_list_password)
            return ask_write
        elif hello == '2':
            len_password = input_len()
            count = input_count()
            get_list_password = create_password(count, len_password)
            ask_write = ask_write_to_file(get_list_password)
            return ask_write
        elif hello == '3':
            len_password = input_len()
            count = input_count()
            get_list_password = create_password(count, len_password)
            ask_write = ask_write_to_file(get_list_password)
            crypt_file = ask_crypt(ask_write)
            return crypt_file
        elif hello == '4':
            name = input('Введите название файла...  ')
            try:
                load_path_to_key = load_key_decrypt()
                decrypt(name, load_path_to_key)
                print('ФАЙЛ РАСШИФРОВАН!!!')
                time.sleep(1.5)
            except Exception as err:
                print('ВОЗНИКЛА ОШИБКА ЧТЕНИЯ КЛЮЧА,ЛИБО ФАЙЛ НЕ ЗАШИФРОВАН!!!\n')
                print(f'ВОТ ВАША ОШИБКА: {err}')

main()
