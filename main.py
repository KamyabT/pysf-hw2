from string import ascii_letters

def encrypt(string, key = 3):
    alphabets = ascii_letters
    result = ""
    for letter in string:
        if letter not in alphabets:
            result += letter
        else:
            new_key = (alphabets.index(letter)+ key) % len(alphabets)
            result += alphabets[new_key]
    print(result)

def decrypt(string, key = 3):
    alphabets = ascii_letters
    decrypt_result = ""
    for letter in string:
        if letter not in alphabets:
            decrypt_result += letter
        else:
            new_key = (alphabets.index(letter)- key) % len(alphabets)
            decrypt_result += alphabets[new_key]
    print(decrypt_result)


encrypting_type = input("what is your cypher type ? Caeser or Pig Pen \n")
user_action = (input("what do you want to do with your text? Encrypt or Decrypt \n"))
user_text = input("please type your text \n")

if encrypting_type.lower() == "caeser" and user_action.lower() == "encrypt":
    encrypt(user_text)
elif encrypting_type.lower() == "caeser" and user_action.lower() == "decrypt":
    decrypt(user_text)
