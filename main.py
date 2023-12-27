import random
import string

def handle_random_password(password_length: int) -> str:
    characters: str = string.ascii_letters
    numbers: str = input('Numbers (y/n)? ')
    if numbers == 'y':
        characters += string.digits
    
    symbols: str = input('Symbols (y/n)? ')
    if symbols == 'y':
        characters += '!"#$%&\'()*+,-./:;<=>?@[]^_{|}~'
    
    return ''.join(random.choice(characters) for _ in range(password_length))


def handle_pin_password(password_length: int) -> str:
    return ''.join(random.choice(string.digits) for _ in range(password_length))

def main() -> None:
    PASSWORD_TYPE: str = input('Password type (random or pin): ')
    PASSWORD_LENGTH: int = int(input('Password length: '))
    password: str

    if PASSWORD_TYPE == 'random':
        password = handle_random_password(PASSWORD_LENGTH)
    elif PASSWORD_TYPE == 'pin':
        password = handle_pin_password(PASSWORD_LENGTH)
    else:
        raise Exception('Unsupported password type')

    print(password)

main()
