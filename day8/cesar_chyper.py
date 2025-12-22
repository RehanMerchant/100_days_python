alphabet = list("abcdefghijklmnopqrstuvwxyz")

direction = input("Enter encode to encrypt and decode to decrypt: ").lower()

text=input("Type your message: ")
shift = int(input("Type the shift number: "))


def encrypt(text,shift):
    chyper_text = ""
    for letter in text:
        shifted_position = (alphabet.index(letter) + shift) % 26
        chyper_text += alphabet[shifted_position]
    print(chyper_text)
    

def decrypt(text,shift):
    real_text = ""
    for letter in text:
        shifted_position = (alphabet.index(letter) - shift) % 26
        real_text += alphabet[shifted_position]
    print(real_text)

  
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("Incorrect Commands")

