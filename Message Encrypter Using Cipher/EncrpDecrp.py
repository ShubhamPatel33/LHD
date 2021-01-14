
def encryption(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 

def decryption(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  

def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        text = input("Enter Text: ")
        s = int(input("Enter Shift: "))
        print("Cipher: " + encryption(text,s))

       
    elif choice == 2:
        text = input("Enter Text: ")
        s = int(input("Enter Shift: "))
        s = 26-s
        print("Cipher: " + decryption(text,s))
    else:
        print("Wrong Choice")


if __name__ == "__main__":
    main()
