import Crypto
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import sys

key = None
with open("key.pem", "rb") as keyFile:
  key = RSA.importKey(keyFile.read())

inputFilename = sys.argv[1]
inputContent = ""
with open(inputFilename, "rb") as inputFile:
  inputContent = inputFile.read()

chunkSize = 128
cipher = PKCS1_v1_5.new(key)
sentinel = Random.new().read(15 + SHA.digest_size)
with open(inputFilename + ".dec", "wb") as outputFile:
  for chunkIndex in range(0, int(len(inputContent) / float(chunkSize))):
    outputFile.write(cipher.decrypt(inputContent[(chunkSize * chunkIndex) : (chunkSize * (chunkIndex + 1))], sentinel))
