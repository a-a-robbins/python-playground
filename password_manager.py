# based on 'Mini Python Projects' by Tech with Tim
# !! This is a PLAY project --- This is NOT a safe password manager, please do not use it as such !!

from cryptography.fernet import Fernet


''' ALREADY USED --- DON'T USE ME AGAIN
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: 
        key_file.write(key)

writeKey()
'''

def loadKey(): 
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = loadKey()
fer = Fernet(key)


def view(): 
    with open("passwords.txt", 'r') as f:
        for line in f.readlines(): 
            data = line.rstrip() #strip off newline
            user, passw = data.split("|")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

def add(): 
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f: 
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True: 
    mode = input("Would you like to add a new password or view existing ones (view, add)? ")

    if mode == "q": 
        break

    elif mode == "view": 
        view()

    elif mode == "add": 
        add()

    else: 
        print("Invalid mode")
        continue