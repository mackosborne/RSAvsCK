#https://github.com/jack4818/kyber-py
#https://cryptopedia.dev/posts/kyber/
from kyber import Kyber512, Kyber768, Kyber1024
import random
import string
import csv
import time
import os
from prettytable import PrettyTable

#Setup file path
outFileName="/home/mack/Desktop/RSAvsCK/outputs/CK_Stream.txt"
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

def veryPrettyPrint(rowlist, times, start, end,limit, version, isTraining, algorithim):
    table= PrettyTable()
    x = 0
#Training Mode
    if(isTraining == 1):
        largest = 0
        for entry in rowlist:
            row = []
            if entry[2] == 1:
                row.append("True") 
            else:
                row.append("False") 
            cryptWords = str(entry[1]).split('\\')
            del cryptWords[0]
            i =0
            for word in cryptWords:
                row.append(word)
                if len(word)-1 > largest:
                    largest = len(word)-1
            data = [i, row]
            table.add_row(data)
            if len(row) > largest:
                largest = len(row)
            i = i + 1
        x = 0
        header = ["ID", "isReal"]
        while x < largest:
            header.append(str(x))
            x = x + 1
        table.field_names = header
        print(table)
        print("Total Time: ", end - start)
        print("Average Time: ", sum(times)/len(times))
        print("Total Entries: ", limit)
        print("Version: ", version)
        print("Algorithim: ", algorithim)
#Testing Mode    
    else:
        for entry in rowlist:
            row = []
            cryptWords = str(entry[1]).split('\\')
            del cryptWords[0]
            for word in cryptWords:
                row.append(word)
            table.add_row(row)
        if len(row) > largest:
                largest = len(row)
        header = ["ID"]
        while x < largest:
            header.append(str(x))
            x = x + 1
        table.field_names = header
        print(table)
        print("Total Time: ", end - start)
        print("Average Time: ", sum(times)/len(times))
        print("Total Entries: ", limit)
        print("Version: ", version)
        print("Algorithim: ", algorithim)
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
    rowlist = []
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
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                quickStart = time.time()
                crypt = real_crypt(KyberChoice, isStatic)
                quickEnd = time.time()
                times.append(quickEnd - quickStart)
                entry = [i, crypt, True]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
    if(method == 2):
        f = open('./outputs/CK_Stream.csv ', 'a')
        writer = csv.writer(f)
        header = ['ID', 'Ciphertext']
        writer.writerow(header)
        for i in range(0, limit):
            num = random.randint(1, 2)
            if(num == 1):
                quickStart = time.time()
                crypt = rand_crypt(KyberChoice)
                quickEnd = time.time()
                times.append(quickEnd - quickStart)
                entry = [i, crypt]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
            if(num == 2):
                quickStart = time.time()
                crypt = real_crypt(KyberChoice, isStatic)
                quickEnd = time.time()
                times.append(quickEnd - quickStart)
                entry = [i, crypt]
                rowlist.append(entry)
                writer.writerow(entry)
                print("Entry: ", entry)
    f.close()
    end = time.time()

    #prettyPrint(rowlist,  times, start, end, limit, isStatic, method, str(KyberChoice))
    #veryPrettyPrint(rowlist, times, start, end, limit, isStatic, method, str(KyberChoice))
    
    print("Total Time: ", end - start)
    print("Average Time: ", sum(times)/len(times))
    print("Done")
        

if __name__ == "__main__":
    '''
    i = 100
    limit = i
    method = 1
    isStatic = 1
    #Pass 1
    KyberChoice = Kyber512
    while i <= 2000:
        generate(KyberChoice, method, isStatic, limit)
        i = i + 100
    #Pass 2
    i = 100
    KyberChoice = Kyber768 
    while i <= 2000:
        generate(KyberChoice, method, isStatic, limit)
        i = i + 100
    #Pass 3
    i = 100
    KyberChoice = Kyber1024
    while i <= 2000:
        generate(KyberChoice, method, isStatic, limit)
        i = i + 100
    '''
      
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
    
    
        