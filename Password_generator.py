import random
import time
from cryptography.fernet import Fernet

def wirte_key():
    key = Fernet.generate_key()
    with open('crypto.key','wb') as key_file:
        key_file.write(key)

def path_to_key(path):
    return open(path,'rb').read()

def load_key():
    return open('crypto.key','rb').read()

def encrypt(key,filename):
    f=Fernet(key)
    with open(filename,'rb') as file:
        file_data =file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename,'wb') as file:
        file.write(encrypted_data)

def decrypt(filename,key):
    f= Fernet(key)
    with open(filename,'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename,'wb') as file:
        file.write(decrypted_data)
        

flag ='y'
while flag.lower():
    test = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()'
    a = [i for i in test]
    password =''
    password_list = list()
    len_pass = 0
    count = 0
    
    while len_pass<=0:
        str_count = 0

        p_count=time.ctime()
        file_name = p_count.strip(' ')+'.txt'
        print(p_count,'>>>>>>>',file_name)
        try:
            len_pass = int(input('Ввведите желаемую длинну пароля\nвведите число...'))
        except:
            print('Введен неверный формат данных,введите число')
    while count<=0:
        try:
            count = int(input('введите количество паролей>>>>'))
        except:
            print("Введите корректные данные,введено не число!")
                
    i=0
    while i<=count-1:
        for x in range(len_pass):
            password+=random.choice(a)
        password_list.append(password)
        password=''
        i+=1
        
    
    for_write = input('Вы хотите записать пароли в файл? нажмите"y",если да')
    for p in password_list:
        if for_write=='y':
            with open(file_name,'a') as file: 
                file.writelines(p+' \n')
        
        else:
            str_count+=1
            print(f'Ваш {str_count}-й пароль : {p}')
    ask_crypt= input('хотите зашифровать Ваши пароли(в случае если вы их записали в файл)?"y"')
    print(file_name)
    if ask_crypt=='y':
        generate_key = input('У Вас есть ключ шифрования? "y" or "n"')
        _='.'
        if generate_key=='n':
            for i in range(5):
                time.sleep(2)
                print(f'Ключ создается{_*i}')
            wirte_key()
            print("Ключ создан")
            encrypt(load_key(),file_name)
            print('файл зашифрован!')
            decrypt_ask= input('Расшифровать файл? "y" or "n"')
            if decrypt_ask=='y':
                for i in range(5):
                    time.sleep(2)
                    print('Процесс расшифровки',_*i)
                decrypt(file_name,load_key())
                print("Файл расшифрован!")
        elif generate_key=='y':
            input_path =input(r'введите путь до ключа')
            print(input_path)
            encrypt(path_to_key(input_path),file_name)

            for i in range(5):
                time.sleep(2)
                print('Процесс расшифровки',_*i)
            print('файл зашифрован!')
            decrypt_ask= input('Расшифровать файл? "y" or "n"')
            if decrypt_ask=='y':
                for i in range(5):
                    time.sleep(2)
                    print('Процесс расшифровки',_*i)
                decrypt(file_name,load_key())
                print("Файл расшифрован!")
        else:
            print('Так как вы не ввели корректный ответ процесс шифрования пропущен')
        
              

    flag = input('Если желаете продолжить нажмите"y",для выхода нажмите любую клавишу!')
    
        
            