import pkcs11

lib = pkcs11.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label='DEMO')

data = b'INPUT DATA'

# Open a session on our token
with token.open(user_pin='1234') as session:
    # Generate an RSA keypair in this session
    pub, priv = session.generate_keypair(pkcs11.KeyType.RSA, 2048)

    # Encrypt as one block
    crypttext = pub.encrypt(data)