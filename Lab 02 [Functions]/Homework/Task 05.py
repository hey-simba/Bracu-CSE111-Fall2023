

def key_generator(*names):
    encrypted_keys = []
    for name in names:
        first_char = name[0].lower()
        last_char = name[-1].upper()
        middle_chars = name[1:-1]
        middle_chars= middle_chars[ : :-1]
        middle_char=""
        for i in middle_chars:
            middle_char+=(str(ord(i)))
        encrypted_key = first_char + middle_char+ last_char
        encrypted_keys.append(encrypted_key)
    return encrypted_keys
key_list = key_generator("Alex", "Bob", "Trudy")
print("Encrypted Keys:", key_list)