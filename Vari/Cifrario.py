from string import ascii_lowercase

def caesar_cipher_encrypt(s: str, key: int):
    s = s.lower()
    result = ""
    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            new_index = index + key
            if new_index >= 26:
                new_index -= 26
            result += ascii_lowercase[new_index]
        else:
            result += char
    return result

def caesar_cipher_decrypt(s: str, key: int):
    s = s.lower()
    result = ""
    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            new_index = index - key
            if new_index < 0:
                new_index += 26
            result += ascii_lowercase[new_index]
        else:
            result += char
    return result

print(caesar_cipher_encrypt("ciao", 2))   
print(caesar_cipher_decrypt("ekcq", 2))     


