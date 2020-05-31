# Double encryptio & decryption
#### Used Caesar & Vernam Ciphers

Implemented for Cryptography course

Vide demo https://streamable.com/t9uqvl

### Explicatie pentru corectare

Pas 1: se cripteaza cu Caesar (`def caesar_encryption(text)`) care are un key generat random `caesar_shift = random.randint(1, 25)`

Pas 2: se cripteaza cu Vernam (`def vernam(text, is_encrypting)`) care are key generata random, care e de aceeasi lungime ca textu intrat `def random_vernam_key(length)`

Pas 3: se decripteaza Vernam, cu aceasi functie, avand aceeasi logica daca ai cheia (XOR intre fiecare bit text/cheie)

Pas 4: se decripteaza Caesar `def caesar_decryption(text):`

Apoi am scris in fisierul `steps_conclusion.txt` toti pasii

Am folosit tkinter pentru GUI, check video demo https://streamable.com/t9uqvl



