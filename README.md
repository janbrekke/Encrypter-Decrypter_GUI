# Encrypter-Decrypter GUI v0.1
Python Script to encrypt and decrypt text strings based on a secret user determined key.\  
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
If you encrypt lots of text and forget the keyword or need to re-create the keyfile you will NOT be able to get the encrypted information back without the correct key.

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