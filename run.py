from arithmetic import arithmetic_example
from hash import hash_function
from symmetric_decrypting import symmetric_decrypting
from symmetric_encrypting import symmetric_encrypting

arithmetic_example(12767,12767,256)
arithmetic_example(1111112424421241111,1111112424421241111,1313)


symmetric_encrypting()
symmetric_decrypting()
print('\n')
hash_function("test_files/text_hash.txt", "test_files/text_hash_copy.txt" )
hash_function("test_files/text_hash.txt", "test_files/text_hash_error.txt")
