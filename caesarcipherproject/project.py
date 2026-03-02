alphabets = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i','o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

def encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key)%26
            cipher_text +=alphabets[new_position]
        else:
            cipher_text += char
    print(f"Here is the text after encryption: {cipher_text}")


def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key)%26
            plain_text +=alphabets[new_position]
        else:
            plain_text += char
    print(f"Here is the text after decryption: {plain_text}")

wanna_end = False
while not wanna_end:
    choice = input(f"Type 'encrypt' for encryption, Type 'decrypt' for 'decryption':\n")
    choice_final = choice.lower()
    txt = input("Type your message:\n")
    text = txt.lower()
    shift = int(input("Type the shift number:\n"))
    length = len(text)
    if choice_final == "encrypt":
        encryption(plain_text = text, shift_key = shift)
    elif choice_final == "decrypt":
        decryption(cipher_text = text, shift_key = shift)
    play_again = input("Type 'Yes' to continue, type 'no' to stop:\n")
    if play_again.lower() == "no":
        wanna_end = True
        print("Thanks for playing!")