from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import string
import random
import csv


#Setup file path
outFileName="/home/mack/Desktop/RSAvsCK/outputs/RSA_Stream.csv"

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
    length = random.randint(1, 100)
    randomstr = ''.join(random.choice(string.ascii_letters) for i in range(length))
    randomstr = randomstr.encode('UTF-8')
    
   

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
    print("ciphertext: ", ciphertext)
    

    #return ciphertext  
    return ciphertext

def real_crypt():
    #Generate a string of real words
    with open('./resources/John_1.txt') as f:
        chosen_line = random.choice(f.readlines())
    f.close
    chosen_line = chosen_line.encode('UTF-8')
    
    

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
    print("ciphertext: ", ciphertext)
    
   

    #return ciphertext
    return ciphertext
def main():
    method = int(input("Training 1, Test 2: "))
    limit = int(input("Enter number of iterations: "))
    rowlist = []
    
    
    if(method == 1):
        f = open('./outputs/RSA_Stream_Training.csv ', 'a')
        writer = csv.writer(f)
        header = ['ID', 'Ciphertext', 'isReal']
        writer.writerow(header)
        for i in range(0, limit):
            num = random.randint(1, 2)
            if(num == 1):
                crypt = rand_crypt()
                entry = [i, crypt, False]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                crypt = real_crypt()
                entry = [i, crypt, True]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
    if(method == 2):
        f = open('./outputs/RSA_Stream.csv ', 'a')
        writer = csv.writer(f)
        header = ['ID', 'Ciphertext']
        writer.writerow(header)
        for i in range(0, limit):
            num = random.randint(1, 2)
            if(num == 1):
                crypt = rand_crypt()
                entry = [i, crypt]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                crypt = real_crypt()
                entry = [i, crypt]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
    f.close()
    print("Done")
    
if __name__ == "__main__":
    main()


    

