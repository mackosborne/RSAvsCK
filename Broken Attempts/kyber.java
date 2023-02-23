import org.bouncycastle.crypto.params.KyberParameters;
import org.bouncycastle.crypto.params.KyberPrivateKeyParameters;
import org.bouncycastle.crypto.params.KyberPublicKeyParameters;
import org.bouncycastle.crypto.params.KyberSecretKeyParameters;
import org.bouncycastle.crypto.params.KyberSharedSecretParameters;
import org.bopuncycastle.crypto.KyberEngine;
import org.bouncycastle.crypto.engines.Kyber768Engine;
import org.bouncycastle.crypto.generators.KyberKeyPairGenerator;
import org.bouncycastle.crypto.generators.KyberParametersGenerator;
import org.bouncycastle.crypto.generators.KyberSecretKeyGenerator;
import org.bouncycastle.crypto.util.Encoding;

import java.security.SecureRandom;

public class KyberExample{
    public static void main(String[] args) {
        KyberParametersGenerator paramsGenerator = new KyberParametersGenerator();
        KyberParameters params = paramsGenerator.generateParameters();

        KyberKeyPairGenerator keyPairGenerator = new KyberKeyPairGenerator();
        keyPairGenerator.init(new KyberParameters(new SecureRandom()));
        keyPairGenerator.init(new KyberParameters(new SecureRandom()));

        //Generate key pair
        KyberPublicKeyParameters publicKey = null;
        KyberPrivateKeyParameters privateKey = null;
        keyPairGenerator.init(new KyberParameters(new SecureRandom()));
        KyberSecretKeyGenerator secretKeyGenerator = new KyberSecretKeyGenerator();
        secretKeyGenerator.init(params);
        for(int i = 0; i <10; i++){
            publicKey = keyPairGenerator.generateKeyPair().getPublic();
            privateKey = keyPairGenerator.generateKeyPair().getPrivate();
        }

        //Generate Random message to encrypt
        byte[] message = new byte[params.getIndcpa().getInBlockBytes()];
        new SecureRandom().nextBytes(message);

        //Encrypt message
        KyberEngine engine = new Kyber768Engine();
        engine.init(true, new KyberPublicKeyParameters(Encoding.decode(publicKey.getEncoded()), params));
        KyberSharedSecretParameters sharedSecret = engine.processBlock(message, 0, message.length);

        //Decrypt message
        engine.init(false, new KyberPrivateKeyParameters(Encoding.decode(privateKey.getEncoded()), params));
        byte[] decryptedMessage = engine.processBlock(sharedSecret.getEncoded(), 0, sharedSecret.getEncoded().length);

        //verify the decrypted message is the same as the original message
        if (!MessageDigest.isEqual(decryptMessage, message)) {
            System.out.println("Decrypted message is not the same as the original message");
            return;
        }
        System.out.println("Decrypted message is the same as the original message");
    }
}