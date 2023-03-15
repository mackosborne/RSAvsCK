from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import string
import random
import csv
import time


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

def real_crypt(mode):
    #Check what mode we are in
    if(mode == 1):
        #Generate a string of real words
        notFound = True
        while notFound:
            with open('./resources/John_1.txt') as f:
                chosen_line = random.choice(f.readlines())
            f.close
            chosen_line = chosen_line.encode('UTF-8')
            #ensure chosen line is less that 190 bytes
            if(len(chosen_line) < 190):
                notFound = False
    else:
        chosen_line = b"Hello World"

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
def generate(version, isTraining,randMode,limit):
    
    start = time.time()
    times = []
    if(isTraining == 1):
        f = open('./outputs/RSA_Stream_Training.csv ', 'a')
        writer = csv.writer(f)
        header = ['ID', 'Ciphertext', 'isReal']
        writer.writerow(header)
        for i in range(0, limit):
            num = random.randint(1, 2)
            if(num == 1):
                quickstart = time.time()
                crypt = rand_crypt()
                quickend = time.time()
                times.append(quickend - quickstart)
                entry = [i, crypt, False]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                quickstart = time.time()
                crypt = real_crypt(randMode)
                quickend = time.time()
                times.append(quickend - quickstart)
                entry = [i, crypt, True]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
    if(isTraining == 2):
        f = open('./outputs/RSA_Stream.csv ', 'a')
        writer = csv.writer(f)
        header = ['ID', 'Ciphertext']
        writer.writerow(header)
        for i in range(0, limit):
            num = random.randint(1, 2)
            if(num == 1):
                quickstart = time.time()
                crypt = rand_crypt()
                quickend = time.time()
                times.append(quickend - quickstart)
                entry = [i, crypt]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                quickstart = time.time()
                crypt = real_crypt(randMode)
                quickend = time.time()
                times.append(quickend - quickstart)
                entry = [i, crypt]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
    f.close()

    end = time.time()
    print("Average Time: ", sum(times)/len(times))
    print("Total Time: ", end - start)
    print("Done")
    
if __name__ == "__main__":
    method = int(input("Training 1, Test 2: "))
    limit = int(input("Enter number of iterations: "))
    randMode = int(input("Set String 1, Random String 2: "))
    rowlist = []
    generate(1,method,randMode,limit)


    

