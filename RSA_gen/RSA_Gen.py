from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import string
import random
import csv
import time
#import resources --prettyPrint.py moved out of resources folder
#import prettyPrint not working> just put junction here
import os


#Setup file path
outFileName="/home/mack/Desktop/RSAvsCK/outputs/RSA_Stream.csv"

def skim(string,i):
    strArray = []
    for letter in string:
        strArray.append(letter)
    strArray[i] = ''
    result = ''.join(strArray)
    return result
        

def prettyPrint(rowlist, times, start, end,limit, version, isTraining, algorithim):
    prevCount = 0
    for file in os.listdir():
        if file.endswith('.txt'):
            prevCount = prevCount + 1
    filename = 'prettyResults' + str(prevCount) + '.txt'
    f = open(filename, 'w+')
    largest_word = 0  
    words = 0      
    for entry in rowlist:
        #Grab each word in ciphertext breaking on \\
        cryptWords = str(entry[1]).split('\\')
        del cryptWords[0]
        if len(cryptWords) > words:
            words = len(cryptWords)
        for word in cryptWords:
            if len(word) > largest_word:
                largest_word = len(word)
    #------ Build Inputs------
    lines = []
    lines1 = "*" * largest_word * words
    lines2 = "* ECRYPTION ALGORITHIM:" + algorithim + " " * (largest_word * words - (len(algorithim) + 22)) + "*" 
    #Calculate White Space
    whiteSpace = largest_word * words - len(lines2)
    lines2 = "*"  + lines2 + " " * int(whiteSpace) + "*"
    lines3 = "* Number of Entries: " + str(limit) + " " * (largest_word * words - 27) + "*"
    lines4 = "* Total Time: " + str(end - start) + " " * (largest_word * words - 20) + "*"
    lines5 = "* Average Time: " + str(sum(times)/len(times)) + " " * (largest_word * words - 20) + "*"
    if isTraining == 1:
        flagged = "True"
    else:
        flagged = "False"
    lines6 = "* Training Mode: " + str(flagged) + " " * (largest_word * words - 19) + "*"
    if version == 1:
        stringVersion = "Static"
    else:
        stringVersion = "Generated"
    lines7 = "* Version: " + str(stringVersion) + " " * (largest_word * words - (11+len(stringVersion))) + "*"
    lines8 = "*" * largest_word * words
    #LABLES
    IDCush = (len(str(limit)) - 2)
    CTCush = (largest_word - 10)/2
    isRealCush = (largest_word - 6)/2

    lines10 = "=" * largest_word * words
    lines11 = "||" + "isReal"  + "|" + " " * int(IDCush) + "ID" + " " * int(IDCush) + "|"
    
    for y in range(words):
        lenNum = len(str(y))
        iBuffer = int(largest_word - lenNum)
        lines11 = lines11 + str(y) + " " * iBuffer + "|"
    #Append Lines
    #* Break
    lines.append(lines1)
    #Encryption Algorithim
    lines.append(lines2)
    #Number of Entries
    lines.append(lines3)
    #Total Time
    lines.append(lines4)
    #Average Time
    lines.append(lines5)
    #Training Mode
    lines.append(lines6)
    #Version
    lines.append(lines7)
    lines.append(lines8)
    #lines.append(lines9)
    lines.append(lines10)
    lines.append(lines11)
    #Append Entries
    if IDCush < 1:
        IDCush = 1
    for entry in rowlist:
        if entry[2] == 1:
            view = "|| True |"+str(entry[0])+ " " * IDCush + "|" 
        else:
            view = "||False |"+str(entry[0])+ " " * IDCush + "|" 
        #Grab each word in ciphertext breaking on \\
        cryptWords = str(entry[1]).split('\\')
        del cryptWords[0]
        for word in cryptWords:
            view = view + str(word) + (" " * (largest_word - len(str(word)))) + "|"
        if isTraining == 1:
            view = view + str(entry[2]) + (" " * (largest_word - len(str(entry[2])))) + "||"
        else:
            view = view + "||"
        lines.append(view)
    lines.append(lines10)
    #Write to file
    for line in lines:
        f.write(line)
        f.write('\n')
    f.close()

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
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
    except:
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
    rowlist = []
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
    algorithim = "RSA"
    prettyPrint(rowlist, times, start, end, limit, randMode, isTraining, algorithim)

    
    print("Average Time: ", sum(times)/len(times))
    print("Total Time: ", end - start)
    print("Done")
    
if __name__ == "__main__":
    #method = int(input("Training 1, Test 2: "))
    method = 1
    #limit = int(input("Enter number of iterations: "))
    limit = 1
    #randMode = int(input("Set String 1, Random String 2: "))
    randMode = 1
    #rowlist = []
    i = 100
    while i <= 2000:
        limit = i
        generate(1,method,randMode,limit)
        i = i + 100
    



    

