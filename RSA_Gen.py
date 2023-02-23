from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import string
import random



def basic_crypt():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    #convert public key to bytes
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    #Encrypt data
    message = b"Hello World"
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Encrypted: ", ciphertext)

def rand_crypt():
    #Generate a random string
    length = random.int(1, 100)
    randomstr = ''.join(random.choice(string.ascii_letters) for i in range(length))
    
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    #convert public key to bytes
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    #Encrypt data
    ciphertext = public_key.encrypt(
        randomstr,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    #Write to file
    with open('RSA_Stream.txt', 'a') as f:
        f.write(ciphertext)
    f.close

def real_crypt():
    #Generate a string of real words
    with open('John_1.txt') as f:
        chosen_line = random.choice(f.readlines())
    f.close

    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    #convert public key to bytes
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    #Encrypt data
    ciphertext = public_key.encrypt(
        chosen_line,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    #Write to file
    with open('RSA_Stream.txt', 'a') as f:
        f.write(ciphertext)
    f.close

def main():
    for i in range(0, 1000):
        num = random.int(1, 2)
        if(num == 1):
            rand_crypt()
        if(num == 2):
            real_crypt()


    

