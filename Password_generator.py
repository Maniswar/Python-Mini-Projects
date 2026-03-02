########        password generator
import random

alphabets = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i','o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', "w", 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'x', 'C', 'V', 'B', 'N', 'M']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '[', ']', ':', ';', "'", '"', '<', '>', ',', '.', '/', '?', '`', '~']
password = ""
password_list = []
print("Welcome to password generator!!!")
lett = input("How many letters you want in your password?: ")
symb = input("How many symbols you want in your password?: ")
numb = input("How many numbers you want in your password?: ")
# print(lett)
# print(symb)
# print(numb)

for i in range(0, int(lett)):
    alpa = password_list.append(random.choice(alphabets))
    alpa = random.choice(alphabets)
    password += alpa
for i in range(0, int(symb)):
    sypa = password_list.append(random.choice(symbols))
    sypa = random.choice(symbols)
    password += sypa
for i in range(0,int(numb)):
    numpa = password_list.append(random.choice(numbers))
    numpa = random.choice(numbers)
    password += numpa
print(password_list)
random.shuffle(password_list)
print("list password: ",password_list)
print("string password: ",password)
shuffledpassword = ""
for i in password_list:
    shuffledpassword += i
print("shuffled password: ",shuffledpassword)