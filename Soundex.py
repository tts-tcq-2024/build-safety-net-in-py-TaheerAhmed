def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def validate_name(name):
    if not name:
        return False
    return True

def initialize_soundex(name):
    return name[0].upper()

def process_characters(name):
    soundex = initialize_soundex(name)
    prev_code = get_soundex_code(soundex)

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        if len(soundex) == 4:
            break

    return soundex

def pad_soundex(soundex):
    return soundex.ljust(4, '0')

def generate_soundex(name):
    if not validate_name(name):
        return ""

    soundex = process_characters(name)
    soundex = pad_soundex(soundex)

    return soundex
