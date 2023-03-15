#requires LIAC-ARFF pip install liac-arff
import csv
import arff
import os
import sys


# csv -> arff for RSA

def morphRSA_Training():
    with open("/home/mack/Desktop/RSAvsCK/outputs/RSA_Stream_Training.csv ", 'r') as fp:
        reader = csv.reader(fp)
        header = None
        data = []
        for row in reader:
            if header is None:
                header = row
            else:
                data.append(row)
    content = {}
    content['relation'] = "from RSA_Stream_Training.csv"
    content['attributes'] = []
    for n in header:
        if n == "ID":
            content['attributes'].append((n, 'NUMERIC'))
            print("added ID")
        elif n == "Ciphertext":
            content['attributes'].append((n, 'STRING'))
            print("added Ciphertext")
        elif n == "isReal":
            content['attributes'].append((n, ['True', 'False']))
            print("added isReal")
        #else error:
        else:
            print("Error reading header in morphRSA_Training")
            exit()
    content['data'] = data
    with open('RSA_STREAM_Training.arff', 'w') as fp:
        arff.dump(content, fp)
    
def morphRSA():
    with open('outputs/RSA_Stream.csv ', 'r') as fp:
        reader = csv.reader(fp)
        header = None
        data = []
        for row in reader:
            if header is None:
                header = row
            else:
                data.append(row)

    content = {}
    content['relation'] = "from RSA_Stream.csv"
    content['attributes'] = []
    for n in header:
        if n == "ID":
            content['attributes'].append((n, 'NUMERIC'))
            print("added ID")
        elif n == "Ciphertext":
            content['attributes'].append((n, 'STRING'))
            print("added Ciphertext")
        #else error:
        else:
            print("Error reading header in morphRSA")
            exit()
    content['data'] = data
    with open('RSA_STREAM.arff', 'w') as fp:
        arff.dump(content, fp)

# csv -> arff for Kyber
def morphCK_Training():
    # csv -> arff for Kyber Training
    with open('/home/mack/Desktop/RSAvsCK/outputs/CK_Stream_Training.csv ', 'r') as fp:
        reader = csv.reader(fp)
        header = None
        data = []
        for row in reader:
            if header is None:
                header = row
            else:
                data.append(row)
    content = {}
    content['relation'] = "from CK_Stream_Training.csv"
    content['attributes'] = []
    for n in header:
        if n == "ID":
            content['attributes'].append((n, 'NUMERIC'))
        elif n == "Ciphertext":
            content['attributes'].append((n, 'STRING'))
        elif n == "isReal":
            content['attributes'].append((n, ['True', 'False']))
        #else error:
        else:
            print("Error reading header in morphCK_Training")
            exit()
    content['data'] = data
    with open('CK_STREAM_Training.arff', 'w') as fp:
        arff.dump(content, fp)

def morphCK():
    # csv -> arff for Kyber Test
    with open('/home/mack/Desktop/RSAvsCK/outputs/CK_Stream.csv ', 'r') as fp:
        reader = csv.reader(fp)
        header = None
        data = []
        for row in reader:
            if header is None:
                header = row
            else:
                data.append(row)
    content = {}
    content['relation'] = "from CK_Stream.csv"
    content['attributes'] = []
    for n in header:
        if n == "ID":
            content['attributes'].append((n, 'NUMERIC'))
        elif n == "Ciphertext":
            content['attributes'].append((n, 'STRING'))
        #else error:
        else:
            print("Error reading header ")
            exit()
    content['data'] = data
    with open('CK_STREAM.arff', 'w') as fp:
        arff.dump(content, fp)

if __name__ == "__main__":
    
    morphRSA_Training()
    morphCK_Training()
    morphCK()
    morphRSA()