#########################################
#                                       #
#            Encrypter\Decrypter        #
#               GUI Software            #
#                                       #
#########################################
# date: 2020/02/27                      #
# name: Jan Brekke                      #
# description: Encrypt and Decrypt text #
# based on a user determined password   #
# created with the key generator.       #
#                                       #
# WARNING!                              #
# DO NOT FORGET the secret password     #
# that you used in the generator!       #
# I am NOT to be held responsible       #
# for any loss you may encouter by      #
# using this python script..            #
# You have been warned!                 #
#########################################

import cryptography, base64, os, os.path
from tkinter import *
from tkinter import messagebox, Menu, ttk
from tkinter.simpledialog import askstring

from os import system, name
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def quit():
    main_window.destroy()

def about():
    messagebox.showinfo('About this Software!', 'Encrypter-Decrypter GUI\n\nCode Language:\nPython\n\nWritten by:\nJan Brekke\n\nhttps://www.digitalbrekke.com')

def clear_decrypt_fields():
    decrypt_output_txt.configure(state='normal')
    decrypt_output_txt.delete(0, END)
    decrypt_input_txt.delete(0, END)
    decrypt_output_txt.configure(state='readonly')

def clear_encrypt_fields():
    encrypt_output_txt.configure(state='normal')
    encrypt_output_txt.delete(0, END)
    encrypt_input_txt.delete(0, END)
    encrypt_output_txt.configure(state='readonly')
    
def copy_decrypted_text_to_clipboard():
    main_window.clipboard_clear()
    decrypt_string = decrypt_output_txt.get()
    main_window.clipboard_append(decrypt_string) 

def copy_encrypted_text_to_clipboard():
    main_window.clipboard_clear()
    encrypt_string = encrypt_output_txt.get()
    main_window.clipboard_append(encrypt_string) 

def keygen():
    password_provided = askstring('Secret Key', 'Enter a personal Key')
    if password_provided is None: # This might be confusing, but it means if cancel is pressed. NOT if field is empty
        messagebox.showwarning('Aborted!', 'User aborted the keygen.')

    elif len(password_provided) == 0: # This is the check for empty field as it checks if the input string is less than 0 characters
        messagebox.showerror('Error', 'I can\'t make a key out of nothing..\nPlease try that again.')
        
    else:
        password = password_provided.encode()
        salt = b'salt_' # Could be changed using a key from os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
            )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        file = open('crypter.key', 'wb')
        file.write(key) # Printing the key to console would show bytes version
        file.close()
        messagebox.showinfo('Complete!', 'Your secret key file (crypter.key)\nhave been successfully created out of the word:\n\n{}'.format(password_provided) + '\n\nIMPORTANT! DO NOT FORGET THIS!\nIf you do, you won\'t be able to\ndecrypt any encrypted text!')

def decrypter():
    if os.path.isfile('crypter.key'):
        file = open('crypter.key', 'rb')
        key = file.read()
        file.close()

        message = decrypt_input_txt.get()
        if len(message) == 0: # This is the check for empty field as it checks if the input string is less than 0 characters
            messagebox.showerror('Error', 'I would need at least something to be able to decrypt..\nPlease try that again.')
            return

        messagedata = message.encode('UTF-8')
        decrypt_output_txt.configure(state='normal')

        #Test if current key will decode
        try:
            f = Fernet(key)
            decrypted = f.decrypt(messagedata)
            decryptedstring = decrypted.decode('UTF-8')

        except cryptography.fernet.InvalidToken:
            messagebox.showerror('ERROR', 'Decryption Error!!\n\nUnable to DeCrypt the input with the secret key stored in crypter.key\n\nThe current KEY does not match..')
            return
        decrypt_output_txt.delete(0, END)
        decrypt_output_txt.insert(0, decryptedstring)
        decrypt_output_txt.configure(state='readonly')

    else:
        messagebox.showwarning('Missing KeyFile', 'Can\'t find any encryption keys!\nYou need to generate a KEY first in File Menu..')
        return


def encrypter():
    if os.path.isfile('crypter.key'):

        file = open('crypter.key', 'rb')
        key = file.read()
        file.close()
        message = encrypt_input_txt.get()
        if len(message) == 0: # This is the check for empty field as it checks if the input string is less than 0 characters
            messagebox.showerror('Error', 'I would need at least something to encrypt..\nPlease try that again.')
            return
        messagedata = message.encode()
        encrypt_output_txt.configure(state='normal')

        f = Fernet(key)
        encrypted = f.encrypt(messagedata)
        encryptedstring = encrypted.decode('ASCII')

        encrypt_output_txt.delete(0, END)
        encrypt_output_txt.insert(0, encryptedstring)
        encrypt_output_txt.configure(state='readonly')
        
    else:
        messagebox.showwarning('Missing KeyFile', 'Can\'t find any encryption keys!\nYou need to generate a KEY first in File Menu..')
        return

#Main Window
main_window = Tk()
main_window.title("Encrypter-Decrypter GUI - DigitalBrekke")
main_window.geometry('640x480')
main_window.iconbitmap('icon.ico')

# importing image, and resize it
logo = PhotoImage(file = r"logo.png") 
logo_fit = logo.subsample(2, 2) 

icon_img = PhotoImage(file = r"icon.png") 
icon_fit = icon_img.subsample(3, 3) 

#The File Menu
menu = Menu(main_window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Generate New Key', command=keygen)
new_item.add_separator()
new_item.add_command(label='About..', command=about)
new_item.add_command(label='Exit', command=quit)
menu.add_cascade(label='File', menu=new_item)
main_window.config(menu=menu)

#Tabs
tab_control = ttk.Notebook(main_window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Decrypt')
tab_control.add(tab2, text='Encrypt')


#Decrypt Tab
tablbl1 = Label(tab1, text= 'Enter the encrypted string that you have\n in the text field below, and press \"DeCrypt\"', font=("Corbel Bold", 12))
tablbl1.grid(column=0, row=0, padx=1, pady=15)

decrypt_input_txt = Entry(tab1, width=30, font=("Corbel Bold", 14))
decrypt_input_txt.grid(column=0, row=2, padx=20)
decrypt_input_btn = Button(tab1, text='Decrypt', font=("Corbel Bold", 16), command=decrypter)
decrypt_input_btn.grid(column=1, row=2)

decrypt_lbl = Label(tab1, text= '\nResult:', font=("Corbel Bold", 16))
decrypt_lbl.grid(column=0, row=3, padx=20)

decrypt_output_txt = Entry(tab1, width=30, font=("Corbel Bold", 14), state="disabled")
decrypt_output_txt.grid(column=0, row=4, padx=20)

copy_decoded_clipboard_btn = Button(tab1, text='Copy to Clipboard', font=("Corbel Bold", 16), command=copy_decrypted_text_to_clipboard)
copy_decoded_clipboard_btn.grid(column=1, row=4)

clear_btn = Button(tab1, text='Clear', font=("Corbel Bold", 16), command=clear_decrypt_fields)
clear_btn.grid(column=0, row=5, pady=10)

#Encrypt Tab
tablbl2 = Label(tab2, text= 'Enter some text in the text field below.\nPress \"EnCrypt\" to encrypt the text.', font=("Corbel Bold", 12))
tablbl2.grid(column=0, row=0, padx=1, pady=15)

encrypt_input_txt = Entry(tab2, width=30, font=("Corbel Bold", 14))
encrypt_input_txt.grid(column=0, row=2, padx=20)
encrypt_input_btn = Button(tab2, text='Encrypt', font=("Corbel Bold", 16), command=encrypter)
encrypt_input_btn.grid(column=1, row=2)

encrypt_lbl = Label(tab2, text= '\nResult:', font=("Corbel Bold", 16))
encrypt_lbl.grid(column=0, row=3, padx=20)

encrypt_output_txt = Entry(tab2, width=30, font=("Corbel Bold", 14), state="disabled")
encrypt_output_txt.grid(column=0, row=4, padx=20)

copy_encoded_clipboard_btn = Button(tab2, text='Copy to Clipboard', font=("Corbel Bold", 16), command=copy_encrypted_text_to_clipboard)
copy_encoded_clipboard_btn.grid(column=1, row=4)

clear_btn2 = Button(tab2, text='Clear', font=("Corbel Bold", 16), command=clear_encrypt_fields)
clear_btn2.grid(column=0, row=5, pady=10)


#TAB Frames
tab_control.pack(expand=1, fill='both')

#Exit Button
btnExit = Button(main_window, text="Exit", font=("Corbel Bold", 16), command=quit)
btnExit.pack( side= RIGHT, pady=20, padx=30 )

#Title at the bottom
lbl = Label(main_window, text="Encrypter-Decrypter GUI\nVersion 0.1", font=("Corbel Bold", 16))
lbl.pack( side= RIGHT, pady=10 )

#Logo at the bottom
logo_lbl = Label(main_window, image = logo_fit)
logo_lbl.pack( side=LEFT, padx=30)

icon_lbl = Label(main_window, image = icon_fit)
icon_lbl.pack( side=LEFT, padx=10)

main_window.mainloop()
