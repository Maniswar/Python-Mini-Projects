choice = input(f"Type 'encrypt' for encryption, Type 'decrypt' for 'decryption':\n")
text = input("Type your message:\n")
shift = input("Type the shift number:\n")
alphabets = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i','o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', "w", 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'x', 'C', 'V', 'B', 'N', 'M']
length = len(text)

def endecrypt():
    if choice == "encrypt":
        input("Type your message:\n")
        input("Type the shift number:\n")
    elif choice == "decrypt":
        input("Type your message:\n")
        input("Type the shift number:\n")


def encryption(plain_txt,shift_key):
    cipher_txt = []
    for i in range(len(plain_txt)):
        cipher_txt.append(plain_txt[i] + shift_key)
    return cipher_txt
def decrypt(plain_txt,shift_):
    cipher_txt = []
    for i in range(len(plain_txt)):
        cipher_txt.append(plain_txt[i] - shift_)
    return cipher_txt