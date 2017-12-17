import random

class Math():
    """
        Responsible for the math part of program
    """
    def prime():
        """
            Generate a prime number and return a random prime number
        """
        primes = []
        for i in range(10000000, 90000000):
            cont = 0
            for j in range(1, i+1):
                if i % j == 0:
                    cont += 1
                else:
                    cont = cont
            if cont == 2:
                primes.append(i)

        temp_prime = random.choice(primes)
        return temp_prime

    def totiene(p, q):
        """
            Calculate a totiene of the two primes number
        """
        pn = (p - 1) * (q -1)
        return pn

    def congruente_modular(e, mod):
        """
            Calculate a modular congruente
        """
        temp = 0
        for num in range(1, mod*1000):
            temp_congruente = e * num
            congruente = temp_congruente -1
            if congruente % mod == 0:
                return num

    def encrypt(m, e, n):
        """
            Encrypt a ascii dec in RSA code and return it
        """
        c = (m**e) % n
        return c

    def decrypt(c, d, n):
        """
            Decrypt a RSA code and return it as a dec
        """
        m = (c**d) % n
        return m

class Rencrypt():
    """
        Responsible for the real encrypt and decrypt RSA code
    """
    def text_to_dec(text):
        """
            Pick up a text and return it as a dec ascii code
        """
        string = ''
        for char in text:
            text_dec = ord(char)
            temp_char = str(text_dec)
            string += temp_char + ' '

        return string[:-1]

    def encrypt(string, e, n):
        """
            Pick up a dec ascii string and return it as a RSA encrypt code
        """
        string = Rencrypt.text_to_dec(string)
        crypt = ''
        for num in string.split(' '):
            num_int = int(num)
            crypt_int = Math.encrypt(num_int, e, n)
            crypt += str(crypt_int) + ' '

        return crypt

    def decrypt(string, d, n):
        """
            Pick up a RSA code string and return it as a alphabet letters
        """
        string_decrypt = ''
        for num in string.split(' '):
            str_int = int(num)
            crypt = Math.decrypt(str_int, d, n)
            string_decrypt += chr(crypt)

        return string_decrypt
