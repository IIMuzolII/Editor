from Banner import banner
from logic import *


def open_file(tip, crypt = ''):
    with open('Encrypt.txt', 'a') as fl:
        fl.write(tip)
        fl.write(crypt+'\n')

if __name__ == '__main__':
    print(banner())
    while 1:
        cmd = int(input(">: "))

        if cmd not in [1, 2, 3, 4, 5, 6] :
            print("Invalid option! Please type a number corresponding an option!")
            continue

        if cmd == 1:
            text = input("Text: ")
            e = int(input("Sub Key: "))
            n = int(input("Key: "))
            crypt = Rencrypt.encrypt(text, e, n)
            print("RSA Code: %s" % crypt)
            open_file("RSA Encrypt: ", crypt)

        elif cmd == 2:
            string = str(input("RSA Code: "))
            d = int(input("Sub Key: "))
            n = int(input("Key: "))
            decrypt = Rencrypt.decrypt(string, d, n)
            print(decrypt)
            open_file("RSA Decrypt: ", decrypt)

        elif cmd == 3:
            prime1 = int(input("First Prime Number: "))
            prime2 = int(input("Second Prime Number: "))
            n = prime1*prime2
            totiene = Math.totiene(prime1, prime2) #Calculate the tortiene of number
            print("Choose a number between 1 and %i" % totiene)
            e = int(input(">: "))
            congruente = Math.congruente_modular(e, totiene)#Calculate the modular congruente
            print("Public Keys  = Key: [%i] Sub key: [%i]" % (n, e))
            print("Private Keys = [%i][%i]Sub Key:[%i]" % (prime1, prime2, congruente))
            open_file("Public Keys = Key: %i; Sub Key: %i" % (n, e))
            open_file("Private Keys = %i; %i; Sub Key %i" % (prime1, prime2, congruente))

        elif cmd == 4:
            print(Math.prime())

        elif cmd == 5:
            with open('Encrypt.txt', 'r') as fl:
                read_file = fl.read()

            print(read_file)

        elif cmd == 6:
            exit()
