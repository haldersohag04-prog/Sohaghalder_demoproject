alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def encryption(plain_text, shift_key):
    cipher_text=""
    for char in plain_text:
            
            
        position = alphabet.index(char)
        new_position = (position + shift_key) % 26
        cipher_text = cipher_text + alphabet[new_position]
    print("your cipher text is :", cipher_text)

def decryption(cipher_text, shift_keys):
    plain_text = ""
    for char in cipher_text:
        position = alphabet.index(char)
        new_position = (position - shift_keys) % 26
        plain_text = plain_text + alphabet[new_position]
    print("your decrypted text is :", plain_text)

user_input = (input("Enter user choice encryption or decryption : "))

if  user_input=="encrypt":
    print("Your choice is encryption: ")
    text=(input("enter your text:"))
    shift=int(input("enter shift key:"))
    encryption(plain_text=text,shift_key=shift)
elif user_input== "decrypt":
    print("your choice is decryption :")
    ciphertext=(input("enter your ciphertext:"))
    shift=int(input("enter shift key:"))
    decryption(cipher_text=ciphertext,shift_keys=shift)
else :
    print("your choice is invalid :")