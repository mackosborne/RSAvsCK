import pkcs11
import os

lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
#How do I define this module to the correct path?
# export PKCS11_MODULE=/Desktop/RSAvsCK/venv/lib/python3.10/site-packages/pkcs11/_pkcs11.cpython-310-x86_64-linux-gnu.so

token = lib.get_token(token_label='DEMO')

data = b'INPUT DATA'

# Open a session on our token
with token.open(user_pin='1234') as session:
    # Generate an RSA keypair in this session
    pub, priv = session.generate_keypair(pkcs11.KeyType.RSA, 2048)

    # Encrypt as one block
    crypttext = pub.encrypt(data)