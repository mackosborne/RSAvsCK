import os
import pkcs11
from pkcs11 import *
import os


# Load the PKCS#11 library
#----- Old Methods -----------------
#lib = pkcs11.lib('/home/mack/.local/lib/python3.10/site-packages/pkcs11/__init__.py')
#PKCS11_MODULE = '/mack/.local/lib/python3.10/site-packages/pkcs11/_pkcs11.cpython-310-x86_64-linux-gnu.so'

#---- We need to set the PKCS11_MODULE environment variable to the path of the PKCS#11 library
#---- This is the path to the PKCS#11 library on my system
#---- You will need to change this to the path on your system
#os.environ['PKCS11_MODULE'] = '/home/mack/.local/lib/python3.10/site-packages/pkcs11/_pkcs11.cpython-310-x86_64-linux-gnu.so'
lib = pkcs11.lib(os.environ['PKCS11_MODULE'])


lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label='DEMO')
data = b'INPUT DATA'

# Open a session on our token
with token.open(user_pin='1234') as session:
    # Generate an RSA keypair in this session
    pub, priv = session.generate_keypair(pkcs11.KeyType.RSA, 2048)

    # Encrypt as one block
    crypttext = pub.encrypt(data)