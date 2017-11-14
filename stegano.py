#!/usr/bin/python3
# -*- coding: utf-8 -*-

############################################################################
#                                ENGLISH                                   #
############################################################################
#                                                                          #
#   Stegano is a free steganography software that aims to hide a string    #
#   in a Bitmap image file                                                 #
#   Copyright (C) 2015  Ronan Boiteau & Cyprien Andres                     #
#                                                                          #
#   This program is free software: you can redistribute it and/or modify   #
#   it under the terms of the GNU General Public License 3 or later, as    #
#   published by the Free Software Foundation.                             #
#                                                                          #
#   This program is distributed in the hope that it will be useful,        #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#   GNU General Public License for more details.                           #
#                                                                          #
#   A copy of the GNU General Public License is provided along with this   #
#   program in the file LICENSE.txt.                                       #
#   You can also read it at <http://www.gnu.org/licenses/gpl-3.0.txt>.     #
#                                                                          #
#   BUG REPORT AND OTHER REQUESTS:                                         #
#   Ronan Boiteau: <ronan@boiteau.ovh>                                     #
#   Cyprien Andres: <andres.cyprien@gmail.com>                             #
#                                                                          #
############################################################################

from tkinter import *
from tkinter.filedialog import askopenfilename
from urllib.request import urlopen

VERSION = "2.0"
VERSION_FLOAT = float(2.0)

def lang_choose():
    """ Display language selection menu """
    clean_frame()
    Label(FRAME, text="\nChoose language").grid(row=0)
    Label(FRAME, text="Choisir langue\n").grid(row=1)
    Button(FRAME, text="English", command=callback_lang_set_en, width=30).grid(row=2)
    Button(FRAME, text="Français", command=callback_lang_set_fr, width=30).grid(row=3)
    Label(FRAME, text="").grid(row=4)
    Button(FRAME, text="Quit / Quitter", command=WIN.destroy, width=30).grid(row=5)

def callback_lang_set_fr():
    """ If french is chosen """
    global LANG
    LANG = "FR"
    callback_show_index()

def callback_lang_set_es():
    """ If spanish is chosen """
    global LANG
    LANG = "ES"
    callback_show_index()

def callback_lang_set_en():
    """ If english is chosen """
    global LANG
    LANG = "EN"
    callback_show_index()

def _(string):
    """ Function that return the translation of a string according to the user's language choice """
    frTranslations = {"Welcome!" : "Bienvenue !", "What can I do for you?" : "Que puis-je faire pour vous ?", "Hide a string in an image" : "Cacher une phrase dans une image", "Retrieve a string from an image" : "Retrouver une phrase dans une image", "Retrieve a string hidden\nwith Stegano 1.X" : "Retrouver une phrase cachée\navec Stegano version 1.X", "Back" : "Retour", "Quit" : "Quitter", "Sure! First let's choose the picture" : "D'accord ! Commencez par choisir l'image", "wherein your string will be hidden" : "dans laquelle votre phrase sera cachée", "GO!" : "C'est parti !", "Bitmap pictures" : "Images bitmap", "Choose a bitmap picture (.bmp)" : "Choisir une image bitmap (.bmp)", "OK! Just choose your picture" : "D'accord ! Choisissez seulement votre", "and I'll find the hidden string" : "image et je trouverai la phrase cachée", "You have to choose a bitmap picture!" : "Vous devez choisir une image bitmap !", "Perfect! What do you want me" : "Parfait ! Que voulez-vous que je", "to hide in this picture?" : "cache dans cette image ?", "Please check the informations" : "Merci de vérifier les informations", "below, then click \"GO!\" or \"Back\" if" : "ci-dessous puis cliquez sur \"C'est parti\"", "you want to correct something" : "ou \"Retour\" pour corriger", "Path to your picture:" : "Chemin de votre l'image :", "String:" : "Phrase :", "Thumbnail of your picture:" : "Miniature de votre image :", "You have to enter something to hide!" : "Vous devez rentrer une phrase à cacher !", "Your image is too small to hide such a\nlong string! Please go back and choose\nanother picture or a smaller string!" : "Votre image est trop petite pour cacher\ncette phrase ! Merci de revenir en\narrière pour choisir une autre\nimage ou une phrase plus courte !", "Your new picture with your\nstring hidden inside is ready!\nYou can find it there on your computer:" : "Votre nouvelle image avec\nvotre phrase cachée dedans est prête !\nVous la trouverez ici sur votre ordinateur :" , "Again" : "Recommencer", "_new.bmp" : "_nouveau.bmp", "String decrypted!\nHere is what I found in your picture:" : "Phrase décryptée !\nVoici ce que j'ai trouvé dans votre image :", "String saved!\nYou can find it here on your computer:" : "Phrase sauvegardée !\nVous la trouverez ici sur votre ordinateur :", "_string.txt" : "_phrase.txt", "Save string to computer" : "Sauvegarder sur mon ordinateur", "Might take a few minutes" : "Peut prendre quelques minutes", "About license..." : "À propos de la licence...", "This program comes with\nABSOLUTELY NO WARRANTY;\nfor details read LICENSE.txt file." : "Ce programme est fourni\nSANS AUCUNE GARANTIE;\npour plus de détails, lisez le\nfichier LICENSE.txt (en anglais).", "This is free software, and you\nare welcome to redistribute\nit under certain conditions;\nread LICENSE.txt file for details." : "Ceci est un programme gratuit, et\nvous êtes invité à le redistribuer\nsous certaines conditions; lisez\nle fichier LICENSE.txt (en anglais)\npour plus de détails."}
    if LANG == "FR":
        try:
            return frTranslations[string]
        except:
            return string
    else:
        return string

def callback_show_index():
    """ Display main menu """
    clean_frame()
    Label(FRAME, text="\n" + _("Welcome!")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=_("What can I do for you?") + "\n").grid(row=1, column=0, columnspan=2)
    Button(FRAME, text=_("Hide a string in an image"), command=callback_hide, width=30).grid(row=2, column=0, columnspan=2)
    Button(FRAME, text=_("Retrieve a string from an image"), command=callback_retrieve, width=30).grid(row=3, column=0, columnspan=2)
    Label(FRAME, text="").grid(row=4, column=0, columnspan=2)
    Button(FRAME, text=_("Retrieve a string hidden\nwith Stegano 1.X"), command=callback_older_version, width=30).grid(row=5, column=0, columnspan=2)
    Button(FRAME, text=_("About license..."), command=callback_about, width=30).grid(row=6, column=0, columnspan=2)
    Label(FRAME, text="").grid(row=7, column=0, columnspan=2)
    Button(FRAME, text=_("Back"), command=lang_choose, width=13).grid(row=8, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=8, column=1)

def callback_about():
    """ Display informations about license """
    clean_frame()
    Label(FRAME, text="\n" + "Stegano " + VERSION + " Copyright (C) 2015\nRonan Boiteau & Cyprien Andres").grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=_("This program comes with\nABSOLUTELY NO WARRANTY;\nfor details read LICENSE.txt file.")).grid(row=1, column=0, columnspan=2)
    Label(FRAME, text=_("This is free software, and you\nare welcome to redistribute\nit under certain conditions;\nread LICENSE.txt file for details.") + "\n").grid(row=2, column=0, columnspan=2)
    Button(FRAME, text=_("Back"), command=callback_show_index, width=13).grid(row=3, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=3, column=1)

def callback_hide():
    """ Function that allows the user to choose the picture wherein the string will be hidden """
    clean_frame()
    Label(FRAME, text="\n" + _("Sure! First let's choose the picture")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=_("wherein your string will be hidden") + "\n").grid(row=1, column=0, columnspan=2)
    Button(FRAME, text=_("Choose a bitmap picture (.bmp)"), command=callback_request_pic_hide, width=30).grid(row=2, column=0, columnspan=2)
    Label(FRAME, text="").grid(row=3, column=0, columnspan=2)
    Button(FRAME, text=_("Back"), command=callback_show_index, width=13).grid(row=4, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=4, column=1)

def callback_retrieve():
    """ Function that allows the user to choose the picture from wich the string will be retrieved """
    clean_frame()
    Label(FRAME, text="\n" + _("OK! Just choose your picture")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=_("and I'll find the hidden string") + "\n").grid(row=1, column=0, columnspan=2)
    Button(FRAME, text=_("Choose a bitmap picture (.bmp)"), command=callback_request_pic_retrieve, width=30).grid(row=2, column=0, columnspan=2)
    Label(FRAME, text="").grid(row=3, column=0, columnspan=2)
    Button(FRAME, text=_("Back"), command=callback_show_index, width=13).grid(row=4, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=4, column=1)

def callback_request_pic_hide():
    """ Opens file browser for the user to select a picture and then check if the image is in Bitmap format """
    global PIC
    PIC = str(askopenfilename(title=_("Choose a bitmap picture (.bmp)"), filetypes=[(_('Bitmap pictures'),'.bmp')]))
    if PIC.endswith(".bmp"):
        clean_frame()
        callback_request_string_hide()
    else:
        Label(FRAME, text=_("You have to choose a bitmap picture!"), fg="red").grid(row=3, column=0, columnspan=2)

def callback_request_pic_retrieve():
    """ Opens file browser for the user to select a picture and then check if the image is in Bitmap format """
    global PIC
    PIC = str(askopenfilename(title=_("Choose a bitmap picture (.bmp)"), filetypes=[(_('Bitmap pictures'),'.bmp')]))
    if PIC.endswith(".bmp"):
        clean_frame()
        callback_check()
    else:
        Label(FRAME, text=_("You have to choose a bitmap picture!"), fg="red").grid(row=3, column=0, columnspan=2)

def callback_check():
    """ Displays summary before decoding and ask for confirmation """
    picDisp = adapt_to_gui(PIC)
    clean_frame()
    Label(FRAME, text="\n" + _("Please check the informations")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=_("below, then click \"GO!\" or \"Back\" if")).grid(row=1, column=0, columnspan=2)
    Label(FRAME, text=_("you want to correct something") + "\n").grid(row=2, column=0, columnspan=2)
    Label(FRAME, text=_("Path to your picture:")).grid(row=3, column=0, columnspan=2)
    Label(FRAME, text=picDisp + "\n", fg="dark green").grid(row=4, column=0, columnspan=2)
    Button(FRAME, text=_("GO!"), command=decode_from_bitmap, width=30).grid(row=5, column=0, columnspan=2)
    Label(FRAME, text=_("Might take a few minutes"), fg="red").grid(row=6, column=0, columnspan=2)
    Button(FRAME, text=_("Back"), command=callback_retrieve, width=13).grid(row=7, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=7, column=1)

def callback_request_string_hide():
    """ Ask the user for a string to hide in the chosen pic """
    global STR_TO_HIDE_ENTRY
    clean_frame()
    Label(FRAME, text="\n" + _("Perfect! What do you want me")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=_("to hide in this picture?") + "\n").grid(row=1, column=0, columnspan=2)
    STR_TO_HIDE_ENTRY = Entry(FRAME, width=33)
    STR_TO_HIDE_ENTRY.grid(row=2, column=0, columnspan=2)
    Button(FRAME, text=_("GO!"), command=callback_get_entry, width=30).grid(row=3, column=0, columnspan=2)
    Label(FRAME, text="").grid(row=4, column=0, columnspan=2)
    Button(FRAME, text=_("Back"), command=callback_hide, width=13).grid(row=5, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=5, column=1)

def callback_get_entry():
    """ Displays summary before decoding and ask for confirmation """
    global STR_TO_HIDE
    STR_TO_HIDE = STR_TO_HIDE_ENTRY.get()
    strDisp = adapt_to_gui(STR_TO_HIDE)
    picDisp = adapt_to_gui(PIC)
    if STR_TO_HIDE != (""):
        clean_frame()
        Label(FRAME, text="\n" + _("Please check the informations")).grid(row=0, column=0, columnspan=2)
        Label(FRAME, text=_("below, then click \"GO!\" or \"Back\" if")).grid(row=1, column=0, columnspan=2)
        Label(FRAME, text=_("you want to correct something") + "\n").grid(row=2, column=0, columnspan=2)
        Label(FRAME, text=_("Path to your picture:")).grid(row=3, column=0, columnspan=2)
        Label(FRAME, text=picDisp + "\n", fg="dark green").grid(row=4, column=0, columnspan=2)
        Label(FRAME, text=_("String:")).grid(row=5, column=0, columnspan=2)
        Label(FRAME, text=strDisp + "\n", fg="dark green").grid(row=6, column=0, columnspan=2)
        Button(FRAME, text=_("GO!"), command=encode_in_bitmap, width=30).grid(row=7, column=0, columnspan=2)
        Label(FRAME, text=_("Might take a few minutes"), fg="red").grid(row=8, column=0, columnspan=2)
        Button(FRAME, text=_("Back"), command=callback_request_string_hide, width=13).grid(row=9, column=0)
        Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=9, column=1)
    else:
        Label(FRAME, text=_("You have to enter something to hide!"), fg="red").grid(row=4, column=0, columnspan=2)

def adapt_to_gui(string):
    """ Function that cut a string so that string will not change the GUI height and then call adapt_width() """
    maxLen = 170
    if len(string) >= maxLen:
        stringStart = string[:-len(string)+69]
        stringEnd = string[len(string)-69:]
        string = adapt_width(stringStart) + "\n[...]\n" + adapt_width(stringEnd)
    else:
        string = adapt_width(string)
    return string

def adapt_width(string):
    """ Function that add line breaks to a string so that string will not change the GUI width """
    maxLen = 30
    if len(string) >= maxLen:
        offset = 0
        while offset < len(string):
            if offset != 0 and offset % maxLen == 0:
                strStart = strEnd = ""
                for i in range(0, offset):
                    strStart += string[i]
                for i in range(offset, len(string)):
                    strEnd += string[i]
                string = strStart + "\n" + strEnd
            offset += 1
    return string

def clean_frame():
    """ Drop all the widget added in the Tkinter frame """
    for widget in FRAME.winfo_children():
        widget.destroy()

def write_new_bitmap_file(bytesArray):
    """ Fonction qui sauvegarde la nouvelle image après encodage et qui affiche la dernière fenêtre de l'interface """
    path = PIC[:-4] + _("_new.bmp")
    pathDisp = adapt_to_gui(path)
    newFile = open(path, "wb")
    newFile.write(bytesArray)
    newFile.close()
    clean_frame()
    Label(FRAME, text="\n" + _("Your new picture with your\nstring hidden inside is ready!\nYou can find it there on your computer:")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=pathDisp + "\n", fg="dark green").grid(row=1, column=0, columnspan=2)
    Button(FRAME, text=_("Again"), command=callback_show_index, width=13).grid(row=9, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=9, column=1)

def display_result():
    """ Displays the retrieved string and offers to save it """
    strDisp = adapt_to_gui(DECRYPTED_STR)
    clean_frame()
    Label(FRAME, text="\n" + _("String decrypted!\nHere is what I found in your picture:")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=strDisp + "\n", fg="dark green").grid(row=1, column=0, columnspan=2)
    Button(FRAME, text=_("Save string to computer"), command=callback_save_string, width=30).grid(row=2, column=0, columnspan=2)
    Label(FRAME, text= "").grid(row=3, column=0, columnspan=2)
    Button(FRAME, text=_("Again"), command=callback_show_index, width=13).grid(row=4, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=4, column=1)

def callback_save_string():
    """ Save the retrieved string in a .txt texte file """
    path = PIC + _("_string.txt")
    pathDisp = adapt_to_gui(path)
    newFile = open(path, "w")
    newFile.write(DECRYPTED_STR)
    newFile.close()
    clean_frame()
    Label(FRAME, text="\n" + _("String saved!\nYou can find it here on your computer:")).grid(row=0, column=0, columnspan=2)
    Label(FRAME, text=pathDisp + "\n", fg="dark green").grid(row=1, column=0, columnspan=2)
    Button(FRAME, text=_("Again"), command=callback_show_index, width=13).grid(row=2, column=0)
    Button(FRAME, text=_("Quit"), command=WIN.destroy, width=13).grid(row=2, column=1)


def encode_in_bitmap():
    """ Main encoding function """
    encryptedStr = encode_bin(encode_hex(STR_TO_HIDE))
    bmpFile = open(PIC, "rb")
    bmpArray = bmpFile.read()
    imageDataOffset = bmpArray[10] + 1
    bitsArray = bytes_to_bits(bmpArray)
    if len(encryptedStr) > len(bitsArray)*2 - imageDataOffset*8:
        Label(FRAME, text=_("Your image is too small to hide such a\nlong string! Please go back and choose\nanother picture or a smaller string!"), fg="red").grid(row=10, column=0, columnspan=2)
    else:
        if len(encryptedStr) > len(bitsArray) - imageDataOffset*8:
            lsb = 2
        else:
            lsb = 1
        bitsArray = array_restore_zeros(bitsArray)
        newBitsArray = put_lsb(bitsArray, imageDataOffset-1, lsb)
        newBitsArray = write_str(bitsArray, encryptedStr, imageDataOffset, lsb)
        newDecArray = bits_to_dec(newBitsArray)
        newBmpArray = bytes(newDecArray)
        write_new_bitmap_file(newBmpArray)
        bmpFile.close()

def put_lsb(array, offset, numberOfBits):
    """ Stores the number of bit(s) used to encode the string at the end of the first bit (after image header) """
    newByte = ""
    for i in range(0,6):
        newByte += array[offset][i]
    if numberOfBits == 1:
        newByte += "0"
    elif numberOfBits == 2:
        newByte += "1"
    array[offset] = newByte
    return array

def bits_to_dec(array):
    """ Translates from binary to decimal values """
    byteArray = []
    for i in range(0, len(array)):
        byteArray.append(int(str(array[i]), 2))
    return byteArray

def write_str(array, string, offset, numberOfBits):
    """ Writes a string in an array that contains 8-bit binary values (using the last 1 or 2 least significant bits) """
    strOffset = 0
    for i in range(offset, len(array)):
        newByte = ""
        arrayOffset = 0
        while arrayOffset < 8-numberOfBits and arrayOffset < len(array[i]):
            newByte += array[i][arrayOffset]
            arrayOffset += 1
        while arrayOffset >= 8-numberOfBits and arrayOffset < len(array[i]):
            if strOffset < len(string):
                newByte += string[strOffset]
                strOffset += 1
                arrayOffset += 1
            else:
                newByte += "0"
                arrayOffset += 1
        array[i] = newByte
    return array

def encode_hex(string):
    """ Translates a string made of regular characters into an hexadecimal string """
    result = []
    for char in string:
        hexStr = hex(ord(char))
        hexStr = hexStr.replace("0x","")
        result.append(hexStr)
    return result

def encode_bin(array):
    """ Translates an hexadecimal string into a binary string """
    for n in range(0, len(array)):
        array[n] = bin(int(array[n], 16))[2:]
        array[n] = str_restore_zeros(array[n], 8)
    result = "".join(array)
    return result

def bytes_to_bits(array):
    """ Translates an array of Bitmap data into an array of binary values """
    bits = []
    for i in range(0, len(array)):
        bits.append(bin(array[i])[2:])
    return bits

def str_restore_zeros(string, bits):
    """ Restore non-significant zeroes in order to easily work with 8 bits binary values (in a string) """
    while len(string) < bits:
        string = "0" + string
    return string

def array_restore_zeros(array):
    """ Restore non-significant zeroes in order to easily work with 8 bits binary values (in an array) """
    for i in range(0, len(array)):
        while len(array[i]) < 8:
            array[i] = "0" + array[i]
    return array


def decode_from_bitmap():
    """ Main decoding function"""
    global DECRYPTED_STR
    bmpFile = open(PIC, "rb")
    bmpArray = bmpFile.read()
    imageDataOffset = bmpArray[10] + 1
    bitsArray = bytes_to_bits(bmpArray)
    bitsArray = array_restore_zeros(bitsArray)
    lsb = find_lsb(bitsArray, imageDataOffset-1)
    bitsArray = sort(bitsArray, imageDataOffset, 8-lsb)
    bitsStr = joiner(bitsArray)
    newArray = []
    for charPos in range(imageDataOffset*8, len(bitsStr)-7, 8):
        newArray.append(bitsStr[charPos] + bitsStr[charPos + 1] + bitsStr[charPos + 2] + bitsStr[charPos + 3] + bitsStr[charPos + 4] + bitsStr[charPos + 5] + bitsStr[charPos + 6] + bitsStr[charPos + 7])
    newArray = decode_bin(newArray)
    DECRYPTED_STR = find_str(newArray)
    display_result()
    bmpFile.close()

def find_lsb(array, offset):
    """ Retrieve the number of bits used to encode the string, it is stored on the first byte after image header """
    if array[offset][7] == "0":
        lsb = 1
    else:
        lsb = 2
    return lsb

def sort(array, offset, firstEncodedBit):
    """ Cuts the first bits of each byte in the array in order to keep only the last bits that contain the hidden message """
    for i in range(offset, len(array)):
        newVar = str("")
        for j in range(firstEncodedBit, 8):
            newVar += array[i][j]
        array[i] = newVar
    return array

def joiner(array):
    """ Pulls the data from an array and put it into a string """
    string = "".join(array)
    return string

def find_str(array):
    """ Function that find characters in an array and put them together into a string """
    string = ""
    for i in range(0, len(array)):
        if array[i] != "\x00":
            string += array[i]
    return string

def decode_bin(array):
    """ Translates an array made of 8-bit binary values into an array of regular characters """
    result = []
    for n in range(0, len(array)):
        result.append(chr(int(array[n], 2)))
    return result


WIN = Tk()
FRAME = Frame(WIN, width=50)
FRAME.pack()
FRAME.master.title("Stegano " + VERSION)
LANG = "EN"
lang_choose()
WIN.mainloop()
