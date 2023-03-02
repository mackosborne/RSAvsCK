import pqcrypto
#https://libpqcrypto.org/install.html
import random
import string
#-----------------------------------------------------------------------------------------------
#- pqcrypto wont install
#- pip install pqcrypto does not work
#- Downloading the tar and installing seemed to work and satisfyied pip, but didnt satisfy import
#- sudo python setup.py install


#- I had to download the tar and install it manually

#- I had to install the following packages
#- sudo apt-get install libffi-dev
#- sudo apt-get install libssl-dev
#- sudo apt-get install python3-dev
#- sudo apt-get install python3-pip
#- sudo apt-get install python3-venv
#- sudo apt-get install python3-wheel
#- sudo apt-get install python3-setuptools
#- sudo apt-get install python3-cffi
#- sudo apt-get install python3-cryptography
#- sudo apt-get install python3-pytest
#- sudo apt-get install python3-pytest-cov



def basic_crypt():
    #generate a keypair
    public_key, private_key = pqcrypto.kyber.generate_keypair()

    #encrypt a message
    message = b"Hello World"
    ciphertext = pqcrypto.kyber.ecrypt(message, public_key)

    print("Encrypted: ", ciphertext)
def rand_crypt():
    #Generate a random string
    length = random.int(1, 100)
    randomstr = ''.join(random.choice(string.ascii_letters) for i in range(length))
    #generate a keypair
    public_key, private_key = pqcrypto.kyber.generate_keypair()

    #encrypt a message
    ciphertext = pqcrypto.kyber.ecrypt(randomstr, public_key)

    #Write to file
    with open('CK_Stream.txt', 'a') as f:
        f.write(ciphertext)
    f.close
def real_crypt():

    #Generate a string of real words
    with open('John_1.txt') as f:
        chosen_line = random.choice(f.readlines())
    f.close

    #generate a keypair
    public_key, private_key = pqcrypto.kyber.generate_keypair()

    #encrypt a message
    ciphertext = pqcrypto.kyber.ecrypt(chosen_line, public_key)

    #Write to file
    with open('CK_Stream.txt', 'a') as f:
        f.write(ciphertext)
    f.close
def main():
    for i in range(0, 1000):
        num = random.int(1, 2)
        if(num == 1):
            rand_crypt()
        if(num == 2):
            real_crypt()
