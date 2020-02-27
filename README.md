# Encrypter-Decrypter GUI v0.1
Python Script to encrypt and decrypt text strings based on a secret user determined key.  
This GUI version is based on the CLI version that you can find here:\
https://github.com/janbrekke/Encrypter-Decrypter


### Prerequisites

You will need some modules to make this work..\
These are defined in the "requirements.txt" file.

```
* cryptography
```
### Installing

To install the Prerequisites, simply run the following command:

```
pip install -r requirements.txt
```
### Usage
Shouldn't be to hard..  
First download the ZIP, or clone the repository using:

```
git clone https://github.com/janbrekke/Encrypter-Decrypter_GUI.git
```
Then start the python file:

```
python encrypt-decrypt_GUI.py
```
Before you can start to encrypt you need to create a KEY file.\
This is done from the "File" menu.\
It will ask you for a secret keyword, type it in and hit OK.\
Now, do NOT forget this keyword!!\
If you encrypt lots of text and forget the keyword, or need to re-create the keyfile but cannot remember what secret keyword you used?  You will NOT be able to get the encrypted information back without the correct key.

You may also notice that the encrypted string is not the same should you encrypt the same word over again.  
This is normal, every encryption will get a uniqe encryption string no matter if its the same word.  
You will be able to decrypt them back to the same word.

Now that you have the KEY file, you can start to encrypt text.

Would suggest you make a copy of this file and store it somewhere should you end up using this software regulary.

### Modify
You are welcome to use this as you wish.\
To change the logo or icon, you simply change them directly in the file.\
Should the new image not fit, just change the ".subsample" value under the comment _"importing image, and resize it"_ \
(Higher number means smaller image..)

Would appreciate on the other hand if the ABOUT section could be left as is.. :stuck_out_tongue:


###  Compatability
Tested on both Windows and Linux (Debian, Ubuntu, Kali, Parrot).\
Should work perfectly fine on both platforms as long as you have the Cryptography installed..\
Also i do not think this will work on Python 2.x\
For more information on Cryptography, please visit: https://cryptography.io/  
For more information on TKinter, please visit: https://docs.python.org/3/library/tk.html

##Q&A
Q: **I have forgotten my secret key, is there a workaround?**  
A: No.. Lose or forget the key, and your FU%¤ED.. Sorry

Q: **Can i use it without a secret key?**  
A: No you can not. The secret key is part of the decryption process. It uses the secret word to create the encryption.

Q: **I want to use this on Windows, can i get it as EXE?**
A: Yes! You need to compile the .py file with a code freezer tool such as "PyInstaller".

Q: **I used your stupid software to encrypt all my passwords, and now it wont decrypt any of them!!**
A: Well, as i am sure this will most likely happen at some point, i did warn you!  
Always read the code before you use it..

Q: **It says "Wrong Key"?**
A: Well, the key used in the first place have most likely been changed. If you remember the secret keyword, you could try to generate the key all over again with the same keyword.

Q: **Can i have your home address so i can beat you up for ruining my passwords?**
A: LuLz! No..

Will add more as they come..  
Thank you, and remember to backup that key file..
