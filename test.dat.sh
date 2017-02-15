python encrypt.py test.dat
python decrypt.py test.dat.enc
diff test.dat test.dat.enc.dec
rm key.pem
rm test.dat.enc
rm test.dat.enc.dec
