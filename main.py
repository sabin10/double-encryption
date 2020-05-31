import random
import string
from tkinter import *
from tkinter import filedialog

""""
CRYPTO LOGIC
"""

ALPHABET_LOWER = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

caesar_encrypted = ''
vernam_encrypted = ''
vernam_decrypted = ''
caesar_decrypted = ''


# Generate Random Caesar Shift
caesar_shift = random.randint(1, 25)


# Generate Random Vernam Key
vernam_key = ''
def random_vernam_key(length):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for i in range(length))



# Caesar Encryption
def caesar_encryption(text):
    encrypted_text = ""
    for char in text:
        if char in ALPHABET_LOWER:
            encrypted_text += ALPHABET_LOWER[(ALPHABET_LOWER.index(char) + caesar_shift) % 26]
        elif char in ALPHABET_UPPER:
            encrypted_text += ALPHABET_UPPER[(ALPHABET_UPPER.index(char) + caesar_shift) % 26]
        else:
            encrypted_text += char
    return encrypted_text


# Caesar Decryption
def caesar_decryption(text):
    decrypted_text = ""
    for char in text:
        if char in ALPHABET_LOWER:
            decrypted_text += ALPHABET_LOWER[(ALPHABET_LOWER.index(char) - caesar_shift) % 26]
        elif char in ALPHABET_UPPER:
            decrypted_text += ALPHABET_UPPER[(ALPHABET_UPPER.index(char) - caesar_shift) % 26]
        else:
            decrypted_text += char
    return decrypted_text


# Vernam Encryption & Decryption
# Function used for both encryption and decryption
def vernam(text, is_encrypting):
    resulted_text = ""
    i_key = 0  # key string's index
    for char in text:
        resulted_text += chr(ord(char) ^ ord(vernam_key[i_key]))
        i_key += 1
    return resulted_text


# Function that handles double encryption and double decryption + writing to file
def start_logic(text):
    file = open('steps_conclusion.txt', 'w')
    file.write('This is the original extracted text: ')
    file.write(text + '\n\n')
    file.write('Steps for double encryption and decryption using Caesar and Vernam algorithms \n\n')

    global vernam_key
    # Generate the key for vernam
    vernam_key = random_vernam_key(len(text))
    text_vernam_key = 'Random generated vernam key = ' + vernam_key + '\n\n'
    file.write(text_vernam_key)

    caesar_encrypted = caesar_encryption(text)
    text_caesar_shift = 'Random caesar shift = ' + str(caesar_shift) + '\n\n'
    text_caesar_encryption = '1. Text after caesar encryption = ' + str(caesar_encrypted) + '\n\n'
    file.write(text_caesar_shift)
    file.write(text_caesar_encryption)

    vernam_encrypted = vernam(caesar_encrypted, is_encrypting=True)
    text_vernam_encryption = '2. Text after Vernam encryption = ' + str(vernam_encrypted) + '\n\n'
    file.write(text_vernam_encryption)

    vernam_decrypted = vernam(vernam_encrypted, is_encrypting=False)
    text_vernam_decryption = '3. Text after Vernam decryption = ' + str(vernam_decrypted) + '\n\n'
    file.write(text_vernam_decryption)

    caesar_decrypted = caesar_decryption(vernam_decrypted)
    file.write('4. Text after Caesar decryption. Should be same as original text \n')
    file.write(caesar_decrypted)

    file.close()


"""
UTILS
"""
def file_to_string(file):
    return open(file).read()


"""
INTERFACE
"""

root = Tk()
root.title('Double encryption')

chosen_file_label = Label(root, text='Choose a .txt file firstly')
encrypt_btn = Button(root, text='Encrypt and Decrypt', state=DISABLED)
conclusion_label = Label(root, text='')


def on_encrypt_pressed():
    conclusion_label.config(text='Encryption & Decryption done. Check steps_conclusion.txt in project directory')
    text = file_to_string(root.filename)
    start_logic(text)


def on_choose_pressed():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    has_selected_file = True if root.filename != '' else False
    if has_selected_file:
        chosen_file_label.config(text='File: ' + root.filename)
        encrypt_btn.config(state='normal')
        encrypt_btn.config(command=on_encrypt_pressed)
    else:
        chosen_file_label.config(text='Try to choose again')


description_label = Label(root, text='Choose a file and then encrypt it with both Caesar and Vernam ciphers').pack()
chosen_file_label.pack()
choose_btn = Button(root, text='Choose a file', command=on_choose_pressed).pack()
encrypt_btn.pack()
conclusion_label.pack()

root.mainloop()
