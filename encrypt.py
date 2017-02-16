import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5
from Crypto.Cipher import PKCS1_v1_5
import sys

key = RSA.generate(1024, Random.new().read)
with open("key.pem", "wb") as keyFile:
  keyFile.write(key.exportKey("PEM", None, 1))

inputFilename = sys.argv[1]
inputContent = ""
with open(inputFilename, "rb") as inputFile:
  inputContent = inputFile.read()

chunkSize = 32
cipher = PKCS1_v1_5.new(key.publickey())
with open(inputFilename + ".enc", "wb") as outputFile:
  for chunkIndex in range(0, int(len(inputContent) / float(chunkSize))):
    outputFile.write(cipher.encrypt(inputContent[(chunkSize * chunkIndex) : (chunkSize * (chunkIndex + 1))]))
  outputFile.write(cipher.encrypt(inputContent[(int(len(inputContent) / float(chunkSize)) * chunkSize) : (len(inputContent))]))
