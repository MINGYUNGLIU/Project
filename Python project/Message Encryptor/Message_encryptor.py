"""
1.Request the user enter a message that is needed to encrypt
2.Generate and display a new key.
3.Display encrypted message. The encrypted string message should be converted to bytes.
4.Display a decrypted message and decrypt the encrypted message.
"""
from cryptography.fernet import Fernet


new_key=Fernet.generate_key()
cipher_suite=Fernet(new_key)

#First encode the message from data type string to bytes then encrypt the message. 
def encrypt_message(message):
    encrypted_message=cipher_suite.encrypt(message.encode())
    return encrypted_message

#First decrypt the bytes message then decode the message from bytes back to string. 
def decrypt_message(message):
    decrypted_message=cipher_suite.decrypt(message).decode()
    return decrypted_message


if __name__=="__main__":
  message=input("Enter a message to encrypt:")
  print("This is a new key:", new_key)
  encrypted_message=encrypt_message(message)
  print("Encrypted Message:",encrypted_message)
  #The argument in the decrypt_message() should be the encrypted message.
  decrypted_message=decrypt_message(encrypted_message)
  print("Decrypted Message:", decrypted_message)

