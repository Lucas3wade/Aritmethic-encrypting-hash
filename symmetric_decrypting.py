from cryptography.fernet import Fernet


def symmetric_decrypting():
    file = open('test_files/key.key', 'rb')
    key = file.read()
    file.close()
    print("Uploaded key: ", key)

    file = open('test_files/test_encrypted.txt', 'rb')
    encrypted = file.read()
    file.close()
    print("Uploaded message: ", encrypted)

    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    print("Decrypted:", decrypted)

    file = open('test_files/test_decrypted.txt', 'wb')
    file.write(decrypted)
    file.close()
