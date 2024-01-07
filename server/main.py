from flask import Flask, request, jsonify
from flask_cors import CORS

import random
import string

app = Flask(__name__)
CORS(app)

def validate_password_type(password_type: str) -> bool:
    return password_type in ('random', 'pin')

def handle_random_password(password_length: int, numbers: bool, symbols: str) -> str:
    characters: str = string.ascii_letters
    if numbers:
        characters += string.digits
    
    characters += symbols
    
    return ''.join(random.choice(characters) for _ in range(password_length))

def handle_pin_password(password_length: int) -> str:
    return ''.join(random.choice(string.digits) for _ in range(password_length))

@app.route('/generate', methods=['POST'])
def main():
    data = request.get_json()
    PASSWORD_TYPE: str = data.get('type', '')
    PASSWORD_LENGTH: int = int(data.get('length', 8))
    include_numbers: bool = data.get('numbers', True)
    symbols: str = data.get('symbols', '')

    if validate_password_type(PASSWORD_TYPE) == False:
        return jsonify({'error': 'Unsupported password type'}), 400

    if PASSWORD_TYPE == 'random':
        password: str = handle_random_password(PASSWORD_LENGTH, include_numbers, symbols)
    else:
        password: str = handle_pin_password(PASSWORD_LENGTH)

    return jsonify({'password': password})

if __name__ == '__main__':
    app.run()
