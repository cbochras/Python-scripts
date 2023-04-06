morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', 
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', 
    ' ': '/'
}

def encode(message):
    encoded = ''  
    for char in message:
        encoded += morse_dict[char.upper()] + ' '
    return encoded

def decode(message):
    message += ' ' # add space to properly split last letter
    decoded = ''
    current_char = ''
    for char in message:  
        if char == ' ':
            if current_char:
                for key, value in morse_dict.items():
                    if value == current_char:
                        decoded += key
                current_char = ''
            else:
                decoded += ' '
        else:
            current_char += char
    return decoded

# Prompt user for input
message = input('Enter a message: ')

# Prompt user for encode/decode choice
choice = input('Enter E to encode or D to decode: ')

# Encode or decode based on user choice
if choice.upper() == 'E':
    encoded = encode(message)
    print(f'{message} encoded: {encoded}')
elif choice.upper() == 'D':
    decoded = decode(message)
    print(f'{message} decoded: {decoded}')
else:
    print('Invalid choice. Please enter E or D.') 
