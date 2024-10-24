import random
import string

def generate_password(length, use_digits=True, use_symbols=True, use_uppercase=True):
    characters = string.ascii_lowercase
    
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Длина?: "))
use_digits = input("Цифры? (да/нет): ").lower() == 'да'
use_symbols = input("Символы? (да/нет): ").lower() == 'да'
use_uppercase = input("Заглавные буквы? (да/нет): ").lower() == 'да'

password = generate_password(length, use_digits, use_symbols, use_uppercase)
print(f"Сгенерированный пароль: {password}")
