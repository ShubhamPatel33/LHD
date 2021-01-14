#Get A Key
from cryptography.fernet import Fernet
key = Fernet.generate_key()


#Store the Key
file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()

#Read the Key
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

#Check for message.txt file

try:
    f = open("message.txt")
    input_file = 'message.txt'
except IOError:
    print("'Message.txt' file not found")
    print("Please Make a 'Message.txt' file and enter the message there.")
finally:
    f.close()


#Encrypt the message


output_file = 'message.encrypted.txt'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the input file

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

print("Encrypted Sucessufully")

with open(output_file, 'wb') as f:
    f.write(encrypted)  # Write the encrypted bytes to the output file



