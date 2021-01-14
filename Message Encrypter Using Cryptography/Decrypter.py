from cryptography.fernet import Fernet,InvalidToken
#Read the key
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

#Decrypt the Message

input_file = 'message.encrypted.txt'
output_file = 'message.decrypted.txt'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the encrypted file

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    print("Decrypted Successfully")

    with open(output_file, 'wb') as f:
        f.write(decrypted)  # Write the decrypted bytes to the output file

except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")
