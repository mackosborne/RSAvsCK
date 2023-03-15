#https://github.com/jack4818/kyber-py
#https://cryptopedia.dev/posts/kyber/
from kyber import Kyber512, Kyber768, Kyber1024
import random
import string
import csv
import time

#Setup file path
outFileName="/home/mack/Desktop/RSAvsCK/outputs/CK_Stream.txt"


def basic_crypt(Kyber):
    s = "Hello World!"
    s.encode('utf-8')

    #generate a keypair (pk, sk)
    pk, sk = Kyber.keygen()
    #generate a challenge and a shared key (c, K)
    c = Kyber.enc(pk,s)

    print("Encrypted: ", c)

def rand_crypt(Kyber):
    #Generate a random string
    length = random.randint(1, 100)
    randomstr = ''.join(random.choice(string.ascii_letters) for i in range(length))
    
    #generate a keypair (pk, sk)
    pk, sk = Kyber.keygen()

    #generate a challenge and a shared key (c, K)
    c = Kyber.enc(pk,randomstr)

    #Return encrypted string
    return c
    
    
def real_crypt(Kyber, method):
    #Check string creation method
    if(method == 1):
        #Generate a string of real words
        with open('/home/mack/Desktop/RSAvsCK/resources/John_1.txt') as f:
            chosen_line = random.choice(f.readlines())
        f.close
    else:
        chosen_line = "Hello World!"
    #generate a keypair (pk, sk)
    pk, sk = Kyber.keygen()
    #generate a challenge and a shared key (c, K)
    c = Kyber.enc(pk,chosen_line)
    #Return encrypted string
    return c


    
def generate(KyberChoice, method, isStatic, limit):

    
        

    start = time.time()
    times = []
    if(method == 1):
        f = open('./outputs/CK_Stream_Training.csv ', 'a')
        writer = csv.writer(f)
        header = ['ID', 'Ciphertext', 'isReal']
        writer.writerow(header)
        for i in range(0, limit):
            num = random.randint(1, 2)
            if(num == 1):
                quickStart = time.time()
                crypt = rand_crypt(KyberChoice)
                quickEnd = time.time()
                times.append(quickEnd - quickStart)
                entry = [i, crypt, False]
                #rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                quickStart = time.time()
                crypt = real_crypt(KyberChoice, isStatic)
                quickEnd = time.time()
                times.append(quickEnd - quickStart)
                entry = [i, crypt, True]
                writer.writerow(entry)
                print("Entry: ", entry)
    if(method == 2):
        f = open('./outputs/CK_Stream.csv ', 'a')
        writer = csv.writer(f)
        header = ['ID', 'Ciphertext', 'isReal']
        writer.writerow(header)
        for i in range(0, limit):
            num = random.randint(1, 2)
            if(num == 1):
                quickStart = time.time()
                crypt = rand_crypt(KyberChoice)
                quickEnd = time.time()
                times.append(quickEnd - quickStart)
                entry = [i, crypt]
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                quickStart = time.time()
                crypt = real_crypt(KyberChoice, isStatic)
                quickEnd = time.time()
                times.append(quickEnd - quickStart)
                entry = [i, crypt]
                writer.writerow(entry)
                print("Entry: ", entry)
    f.close()
    end = time.time()
    print("Total Time: ", end - start)
    print("Average Time: ", sum(times)/len(times))
    print("Done")
        

if __name__ == "__main__":
    #Select Kyber Version
    select = int(input("Enter 1 or nothing for Kyber512, 2 for Kyber768, 3 for Kyber1024: "))
    #Select Training or Testing  
    method = int(input("Training 1, Test 2: "))
    #Select string creation method      
    isStatic = int(input("Static Gen 1, Random Gen 2: "))
    #Select number of iterations
    limit = int(input("Enter number of iterations: "))
    if(select == 1):
        KyberChoice = Kyber512
    if(select == 2):
        KyberChoice = Kyber768  
    if(select == 3):
        KyberChoice = Kyber1024
    else:
        KyberChoice = Kyber512
    generate(KyberChoice, method, isStatic, limit)