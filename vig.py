# vig.py is a Vigenere Cipher Tool started by Aggredicus on 3/30/18
# Feel free to adapt these simple tools to your own purposes, but please credit me (Aggredicus) while doing so!

# The tkinter GUI was adapted from the tkinter documentation at the following URL: http://www.tkdocs.com/tutorial/firstexample.html#code
# Tkinter Docs Attribution below:
# "All material on this site is Copyright (C) 2007-2017 Mark Roseman. This work is licensed under a Creative Commons Attribution-Noncommercial-Share Alike 2.5 Canada License. If you have any questions regarding the use of the material on this site, including possible uses not covered by the license, please don't hesitate to email Mark."

from tkinter import *
from tkinter import ttk
from random import randint

# Caeser Cipher

# Converts a string containing a letter into an integer representation
def num_encrypt(arg):
    if (arg.isalpha() == True):
        lowercase_letter = arg.lower()
        letter_code = ord(lowercase_letter) - 96
        return int(letter_code)
    else:
        return str(arg)
    
# Converts an integer representation of a letter into a string containing a letter
def num_decrypt(arg):
    # Checks to see if arg is a non-integer
    if (isinstance(arg, int) != True):
        print('num_decrypt received a non-integer of value ' + arg)
        return arg
    else:
        # The letter_code variable used to be for converting to int, but I kept it for
        # aesthetic reasons after implementing the section above.
        lowercase_letter = chr(arg + 96)
        return lowercase_letter

# Shifts a letter <shift_value> places to the right for each letter
def czr_encrypt(shift_value, letter):
    if (letter.isalpha() == False):
        return letter
    else:
        letter_to_num = num_encrypt(str(letter))
        shifted_num = letter_to_num + shift_value
        # Handles cipher shifts past z
        if (shifted_num > 26):
            shifted_num -= 26
        # Handles cipher shifts before a
        elif (shifted_num < 1):
            shifted_num += 26
        num_to_letter = num_decrypt(shifted_num)
        return num_to_letter

# Shifts a letter <shift_value> places to the left for each letter
def czr_decrypt(shift_value, letter):
    if (letter.isalpha() == False):
        return letter
    else:
        letter_to_num = num_encrypt(str(letter))
        shifted_num = letter_to_num - shift_value
        # Handles cipher shifts past z
    if (shifted_num > 26):
        shifted_num -= 26
    # Handles cipher shifts before a
    elif (shifted_num < 1):
        shifted_num += 26
    num_to_letter = num_decrypt(shifted_num)
    return num_to_letter

# Takes in the Caeser shift value and a full string to shift the full string <shift_value> places to the right
def czr_full_encrypt(shift_value, full_string):
    arr = list(full_string)
    encrypted_arr = []
    i = 0
    while i < len(arr):
        encrypted_arr.append(czr_encrypt(shift_value, arr[i]))
        i += 1
    final_string = ''.join(encrypted_arr)
    return final_string

# Takes in a key string and a message string to encrypt a message using a Vigenere cipher
def vig_full_encrypt(key_string, message_string):
    key_arr = list(key_string)
    full_arr = list(message_string)
    
    # If key is shorter than message, repeats the key to match the length of the message
    if (len(key_arr) < len(full_arr)):
        extended_key_arr = []
        whole_keys = len(full_arr) / len(key_arr)
        partial_key_letters = len(full_arr) % len(key_arr)
        k = 0
        l = 0
        
        # Repeats the key string <whole_keys> number of times
        while k < whole_keys:
            
            # Appends the letters of the key string, one at a time
            m = 0
            while m < len(key_arr):
                extended_key_arr.append(key_arr[m])
                m += 1
            k += 1
        
        # Appends the letters of the key string, one at a time, as many times as it takes
        # to match the key string length to the message string length
        while l < partial_key_letters:
            extended_key_arr.append(key_arr[l])
            l += 1
        
        # Replaces key_arr with extended_key_arr
        key_arr = extended_key_arr
    
    # Performs the Vigenere cipher by Caeser shifting each letter in the message string according
    # to the integer value of letter correspondingly positioned in the key string
    coded_arr = []
    j = 0
    while j < len(full_arr):
        coded_arr.append(czr_encrypt(num_encrypt(str(key_arr[j])), str(full_arr[j]))) 
        j += 1
    coded_string = ''.join(coded_arr)
    return coded_string

# The same as vig_full_encrypt(), except that it performs the Caser shift in the other direction
def vig_full_decrypt(key_string, message_string):
    key_arr = list(key_string)
    full_arr = list(message_string)
    
    # If key is shorter than message, repeats the key to match the length of the message
    if (len(key_arr) < len(full_arr)):
        extended_key_arr = []
        whole_keys = len(full_arr) / len(key_arr)
        partial_key_letters = len(full_arr) % len(key_arr)
        k = 0
        l = 0
        
        # Repeats the key string <whole_keys> number of times
        while k < whole_keys:
            
            # Appends the letters of the key string, one at a time
            m = 0
            while m < len(key_arr):
                extended_key_arr.append(key_arr[m])
                m += 1
            k += 1
        
        # Appends the letters of the key string, one at a time, as many times as it takes
        # to match the key string length to the message string length
        while l < partial_key_letters:
            extended_key_arr.append(key_arr[l])
            l += 1
        
        # Replaces key_arr with extended_key_arr
        key_arr = extended_key_arr
    
    # Performs the Vigenere cipher by Caeser shifting each letter in the message string according
    # to the integer value of letter correspondingly positioned in the key string
    coded_arr = []
    j = 0
    while j < len(full_arr):
        # Here, I have negated the num_encrypt() result to decrypt instead of encrypt
        coded_arr.append(czr_encrypt(-num_encrypt(str(key_arr[j])), str(full_arr[j]))) 
        j += 1
    coded_string = ''.join(coded_arr)
    return coded_string

# Generates a key of random letters based on an integer key length argument
# REQUIRES: random.randint
def random_key(key_length):
    random_key_arr = []
    while key_length > 0:
        random_key_arr.append(num_decrypt(randint(1, 26)))
        key_length -= 1
    random_key_string = ''.join(random_key_arr)
    return random_key_string
    
# Note: It might be useful to translate the key 

# Tkinter GUI

def czr_gui_encrypt(*args):
    try:
        input_string = str(message.get())
        input_shift = int(shift.get())
        message_encrypted.set(czr_full_encrypt(input_shift, input_string))
    except ValueError:
        pass

def vig_gui_encrypt(*args):
    try:
        input_string = str(message.get())
        input_key = str(key.get())
        message_encrypted.set(vig_full_encrypt(input_key, input_string))
    except: ValueError:
        pass

def vig_gui_decrypt(*args):
    try:
        input_string = str(message.get())
        input_key = str(key.get())
        message_encrypted.set(vig_full_decrypt(input_key, input_string))
    except: ValueError:
        pass


# Copies message_encrypted to the clipboard to be pasted
# NOTE: You cannot paste the message from the clipboard after the window is closed on test OS
def copy_to_clipboard(*args):x
    try:
        input_message_encrypted = str(message_encrypted.get())
        root.clipboard_clear()
        root.clipboard_append(input_message_encrypted)
        root.update()
    except ValueError:
        pass
    
root = Tk()
root.title("Caeser Shift Tool")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

shift = StringVar()
message = StringVar()
message_encrypted = StringVar()

shift_entry = ttk.Entry(mainframe, width=3, textvariable=shift)
shift_entry.grid(column=2, row=1, sticky=(W))
message_entry = ttk.Entry(mainframe, width=7, textvariable=message)
message_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=message_encrypted).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Encrypt", command=czr_gui_encrypt).grid(column=3, row=2, sticky=W)

ttk.Button(mainframe, text="Copy to Clipboard", command=copy_to_clipboard).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text='Shift Value:').grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Message:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Encrypted message:").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

shift_entry.focus()
root.bind('<Return>', czr_gui_encrypt)

root.mainloop()
