# Encrypter-Decrypter GUI v0.1
Python Script to encrypt and decrypt text strings based on a secret user determined key.  
This GUI version is based on the CLI version that you can find here:\
https://github.com/janbrekke/Encrypter-Decrypter


### Prerequisites

If not using the EXE file, you'll need some modules to make this work..\
These are defined in the "requirements.txt" file.

```
* cryptography
```
### Installing

To install the Prerequisites, simply run the following command:

```
pip install -r requirements.txt
```
### Usage Pyton file
Shouldn't be to hard..  
First download the ZIP, or clone the repository using:

```
git clone https://github.com/janbrekke/Encrypter-Decrypter_GUI.git
```
Then start the python file (with python3):

```
python encrypt-decrypt_GUI.py
```

### Usage EXE file
Well, just download ALL the content in the bin folder, or just grab the ZIP file you see above.\
Double click the exe file and violã!

#### Additional usage info
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


### Compatability
Tested on both Windows and Linux (Debian, Ubuntu, Kali, Parrot).\
Should work perfectly fine on both platforms as long as you have the Cryptography installed..\
Also i do not think this will work on Python 2.x\
For more information on Cryptography, please visit: https://cryptography.io/  
For more information on TKinter, please visit: https://docs.python.org/3/library/tk.html

## Q&A
Q: **I have forgotten my secret key, is there a workaround?**  
A: No.. Lose or forget the key, and your FU%¤ED.. Sorry!

Q: **Can i use it without a secret key?**  
A: No you can not. The secret key is part of the encryption process. It uses the secret word to create the encryption string.

Q: **I want to use this on Windows, can i get it as EXE?**  
A: Yes! You need to compile the .py file with a code freezer tool such as "PyInstaller".
   Or you can find it in the "Bin" folder.
   REMEMBER to keep the RES folder together with the EXE file.

Q: **It says "Failed to execute script"**\
A: The EXE file should be in a folder. Then in this same folder there should be another folder called "res".
   If this res folder is not there the EXE refuses to start.
   ALSO if any of the 3 items "logo.png, icon.png, icon.ico" inside the res folder is missing, the EXE will refuse to start.
   So don't seperate the EXE and the res folder. They are lovers <3

Q: **It says "Wrong Key"?**  
A: Well, the key used in the first place have most likely been changed. If you remember the secret keyword, you could try to generate the key all over again with the same keyword.

Q: **Can i modify it to my needs?**  
A: Sure! I believe in a free world. Go nuts!  
I ask that you keep the About popup as it is though as i did spend some time on this.  
At least mention me as a source somewhere..... :pray:

Q: **I used your stupid software to encrypt all my passwords, and now it wont decrypt any of them!!**  
A: Well, as i am sure this will most likely happen at some point, i did warn you!  
Always read the code before you use it..

Q: **Can i have your home address so i can beat you up for ruining my passwords?**  
A: LuLz! No..

Will add more as they come..  
Thank you, and remember to backup that key file..
