import hashlib


def hash_function(first_file, second_file):

    file = open(first_file, 'rb')
    first_message = file.read()
    first_message_hash = hashlib.sha1(first_message)

    file2 = open(second_file, 'rb')
    second_message = file2.read()
    second_message_hash = hashlib.sha1(second_message)

    print(first_message_hash.hexdigest())
    print(second_message_hash.hexdigest())

    if first_message_hash.hexdigest() == second_message_hash.hexdigest():
        print("The same hashes")
    else:
        print("Not the same hashes")
Basic aritmethic operations, symmetric encrypting and decrypting text from text files, hash function.