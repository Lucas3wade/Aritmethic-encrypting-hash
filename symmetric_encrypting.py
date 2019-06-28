from cryptography.fernet import Fernet


def symmetric_encrypting():

    key = Fernet.generate_key()
    file = open('test_files/key.key', 'wb')
    file.write(key)
    file.close()
    print("Key: ", key)

    # key generated

    file = open('test_files/test.txt', 'rb')
    message = file.read()
    file.close()
    print("Message: ", message)

    f = Fernet(key)
    encrypted = f.encrypt(message)
    print("Encrypted: ", encrypted)

    file = open('test_files/test_encrypted.txt', 'wb')
    file.write(encrypted)
    file.close()
