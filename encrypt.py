from cryptography.fernet import Fernet

with open('.\\Config\\Enc.key', 'rb') as Enc:
    key = Enc.read()
f = Fernet(key)
with open(".\\Config\\dec_db.txt", "rb") as decrypted_file:
    decrypted = decrypted_file.read()
encrypted = f.encrypt(decrypted)
with open('.\\Config\\enc_db.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
