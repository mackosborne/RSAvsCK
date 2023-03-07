#requires LIAC-ARFF pip install liac-arff
import csv
import arff


# csv -> arff for RSA
def morphRSA():
    with open('RSA_Stream.csv', 'r') as fp:
        reader = csv.reader(fp)
        header = None
        data = []
        for row in reader:
            if header is None:
                header = row
            else:
                data.append(row)

    content = {}
    content['relation'] = "from my csv file"
    content['attributes'] = []
    for n in header:
        if n == "isReal":
            content['attributes'].append((n, ['True', 'False']))
        else:
            content['attributes'].append((n, 'NUMERIC'))
    content['data'] = data
    with open('RSA_STREAM.arff', 'w') as fp:
        arff.dump(content, fp)

def morphRSA_Training():
    with open('RSA_Stream_Training.csv', 'r') as fp:
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
        if n == "Ciphertext":
            content['attributes'].append((n, 'STRING'))
        if n == "isReal":
            content['attributes'].append((n, ['True', 'False']))
        #else error:
        else:
            print("Error reading header")
            exit()
    content['data'] = data
    with open('RSA_STREAM_Training.arff', 'w') as fp:
        arff.dump(content, fp)
    

def morphCK_Training():
    # csv -> arff for Kyber Training
    with open('CK_Stream.csv', 'r') as fp:
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
        if n == "Ciphertext":
            content['attributes'].append((n, 'STRING'))
        if n == "isReal":
            content['attributes'].append((n, ['True', 'False']))
        #else error:
        else:
            print("Error reading header")
            exit()
    content['data'] = data
    with open('CK_STREAM.arff', 'w') as fp:
        arff.dump(content, fp)

def morphCK_Test():
    # csv -> arff for Kyber Test
    with open('CK_Stream_Test.csv', 'r') as fp:
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
        if n == "Ciphertext":
            content['attributes'].append((n, 'STRING'))
        #else error:
        else:
            print("Error reading header")
            exit()
    content['data'] = data
    with open('CK_STREAM_TEST.arff', 'w') as fp:
        arff.dump(content, fp)

if __name__ == "__main__":
    morphRSA()
    morphRSA_Training()
    morphCK_Training()
    morphCK_Test()