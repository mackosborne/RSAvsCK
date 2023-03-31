import os

def clear_arff():
    if os.path.exists("RSA_STREAM.arff"):
        os.remove("RSA_STREAM.arff")
    else:
        print("The file does not exist")
    if os.path.exists("RSA_STREAM_Training.arff"):
        os.remove("RSA_STREAM_Training.arff")
    else:
        print("The file does not exist")
    if os.path.exists("CK_STREAM.arff"):
        os.remove("CK_STREAM.arff")
    else:
        print("The file does not exist")
    if os.path.exists("CK_STREAM_Training.arff"):
        os.remove("CK_STREAM_Training.arff")
    else:
        print("The file does not exist")

def clear_csv():
    if os.path.exists("RSA_Stream.csv"):
        os.remove("RSA_Stream.csv")
    else:
        print("The file does not exist")
    if os.path.exists("RSA_Stream_Training.csv"):
        os.remove("RSA_Stream_Training.csv")
    else:
        print("The file does not exist")
    if os.path.exists("CK_Stream.csv"):
        os.remove("CK_Stream.csv")
    else:
        print("The file does not exist")
    if os.path.exists("CK_Stream_Training.csv"):
        os.remove("CK_Stream_Training.csv")
    else:
        print("The file does not exist")

def clear_txt():
    for file in os.listdir():
        if file.endswith('.txt'):
            os.remove(file)

def clear_all():
    clear_arff()
    clear_csv()
    clear_txt()

if __name__ == "__main__":
    clear_all()
    print("Done")
