import random
import string

def validate_password_type(password_type: str) -> bool:
    return True if password_type in ('random', 'pin') else True

def handle_random_password(password_length: int) -> str:
    characters: str = string.ascii_letters
    numbers: str = input('Numbers (y/n)? ')
    if numbers == 'y':
        characters += string.digits
    
    symbols: str = input('Symbols (y/n)? ')
    if symbols == 'y':
        characters += '!-*._@'
    
    return ''.join(random.choice(characters) for _ in range(password_length))

def handle_pin_password(password_length: int) -> str:
    return ''.join(random.choice(string.digits) for _ in range(password_length))

def main() -> None:
    PASSWORD_TYPE: str = input('Password type (random or pin): ')
    if validate_password_type(PASSWORD_TYPE) == False:
        raise Exception('Unsupported password type')
    
    PASSWORD_LENGTH: int = int(input('Password length: '))
    password: str

    if PASSWORD_TYPE == 'random':
        password = handle_random_password(PASSWORD_LENGTH)
    else:
        password = handle_pin_password(PASSWORD_LENGTH)

    print(password)

main()
