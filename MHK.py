from random import randint
from gmpy2 import invert
import time


MAX_CHARS = 150
BINARY_LENGTH = MAX_CHARS * 8

class MHK_Crypto_w_Arrays:

    def __init__(self):
        self.b = []
        self.w = []
        self.q = 0
        self.r = 0
        self.genKeys()

    def genKeys(self):
        maxBits = 50

        self.w.append(randint(1, 2**maxBits))
        sum = self.w[0]
        for i in range(1, BINARY_LENGTH):
            self.w.append(sum + randint(1, 2**maxBits))
            sum += self.w[i]

        self.q = sum + randint(1, 2**maxBits)
        self.r = self.q - 1
        for i in range(BINARY_LENGTH):
            self.b.append((self.w[i]*self.r)%self.q)

    # @profile
    def encryptMsg(self, message):

        if len(message) > MAX_CHARS:
                print("\nYour message should have at most ", MAX_CHARS, "characters! Please try again.\n\n")
        elif len(message) <= 0:
                print("\nYou message should not be empty! Please try again.\n\n")


        msgBinary = ''.join('{:08b}'.format(b) for b in message.encode('utf8'))

        if len(msgBinary) < BINARY_LENGTH:
            msgBinary = msgBinary.zfill(BINARY_LENGTH)


        result = 0
        
        for i in range(len(msgBinary)):
            result += self.b[i]*int(msgBinary[i],2)

        return str(result)

    def decryptMsg(self, ciphertext):

        decrypted_binary = ''
        ciphertext = int(ciphertext)

        tmp = (ciphertext*invert(self.r,self.q))%self.q

        for i in range(len(self.w)-1,-1,-1):
            if self.w[i] <= tmp:
                tmp -= self.w[i]
                decrypted_binary += '1'
            else:
                decrypted_binary += '0'
        


        return int(decrypted_binary[::-1], 2).to_bytes((len(decrypted_binary) + 7) // 8, 'big').decode()

if __name__ == "__main__":
    
    encrypt_time=0
    decrypt_time=0
    f = open("test.txt", "r")
    messages = f.read().splitlines()
    
    start_keygen=time.process_time()
    crypto = MHK_Crypto_w_Arrays()
    end_keygen=time.process_time()

    keygen_time= end_keygen-start_keygen
 
    for message in messages:
        
 
       
        while True:
           
            if len(message) > MAX_CHARS:
                print("\nYour message should have at most ", MAX_CHARS, "characters! Please try again.\n\n")
            elif len(message) <= 0:
                print("\nYou message should not be empty! Please try again.\n\n")
            else:
                break

        
        start_encrypt = time.process_time()
        encrypted = crypto.encryptMsg(message)
        end_encrypt = time.process_time()
        
        encrypt_time += end_encrypt-start_encrypt

        
        
        start_decrypt = time.process_time()
        decrypted = crypto.decryptMsg(encrypted)
        end_decrypt = time.process_time()
        
        decrypt_time += end_decrypt-start_decrypt
        

    f.close()
    print("Total Time for encryption is ",encrypt_time)
    print("Total Time for decryption is ",decrypt_time)
    print("Total Time for key generation is ",keygen_time)
    

