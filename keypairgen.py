import pkcs11

# the key_id has to be the same for both objects
key_id = (0x22,)

pkcs11 = PyKCS11Lib()
pkcs11.load()  # define environment variable PYKCS11LIB=YourPKCS11Lib

# get 1st slot
slot = pkcs11.getSlotList(tokenPresent=True)[0]

session = pkcs11.openSession(slot, CKF_SERIAL_SESSION | CKF_RW_SESSION)
session.login("1234")

pubTemplate = [
    (CKA_CLASS, CKO_PUBLIC_KEY),
    (CKA_TOKEN, CK_TRUE),
    (CKA_PRIVATE, CK_FALSE),
    (CKA_MODULUS_BITS, 0x0400),
    (CKA_PUBLIC_EXPONENT, (0x01, 0x00, 0x01)),
    (CKA_ENCRYPT, CK_TRUE),
    (CKA_VERIFY, CK_TRUE),
    (CKA_VERIFY_RECOVER, CK_TRUE),
    (CKA_WRAP, CK_TRUE),
    (CKA_LABEL, "My Public Key"),
    (CKA_ID, key_id),
]

privTemplate = [
    (CKA_CLASS, CKO_PRIVATE_KEY),
    (CKA_TOKEN, CK_TRUE),
    (CKA_PRIVATE, CK_TRUE),
    (CKA_DECRYPT, CK_TRUE),
    (CKA_SIGN, CK_TRUE),
    (CKA_SIGN_RECOVER, CK_TRUE),
    (CKA_UNWRAP, CK_TRUE),
    (CKA_ID, key_id),
]

(pubKey, privKey) = session.generateKeyPair(pubTemplate, privTemplate)

# logout
session.logout()
session.closeSession()