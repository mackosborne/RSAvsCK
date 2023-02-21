import pqcrypto.kyber

#generate a keypair
#public_key, private_key = pqcrypto.kyber.kyber_512_90s.keypair()
public_key, private_key = pqcrypto.kyber.generate_keypair()

#encrypt a message
message = b"Hello World"
ciphertext = pqcrypto.kyber.ecrypt(message, public_key)

print("Encrypted: ", ciphertext)