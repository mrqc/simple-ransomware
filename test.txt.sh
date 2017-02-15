python encrypt.py test.txt
python decrypt.py test.txt.enc
diff test.txt test.txt.enc.dec
rm key.pem
rm test.txt.enc
rm test.txt.enc.dec
