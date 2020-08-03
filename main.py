# Encrypt and unEncrypt
import platform
from os import system
#===================================
def sysName():  # git system name ( Windows / Linux )
    sysName = platform.system()
    return sysName

def screenClear():
    if sysName() == 'Linux':
        cln = system('clear')
    else:
        cln = system('cls')

def _enc():
    _msg = input ('Text for Encrypt it : ')
    _key = input ('Enter the encryption key,to help [3]  : ')
    msgList = list(_msg.strip())
    encMsg =[]
    enctxt = ''
    for i in msgList:
        encMsg.append(ord(i)-int(_key))
    for t in encMsg:
        enctxt += (f'{chr(int(t))}')
    return enctxt


def _unenc():
    _msg = input ('Message for Unencrypt it : ')
    _key = input ('Enter the encryption key : ')
    msgList = list(_msg.strip())
    encMsg =[]
    txt = ''
    for i in msgList:
        encMsg.append(ord(i)-int(_key))
    for t in encMsg:
        txt += (f'{chr(int(t))}')
    return txt

def _help():
    screenClear()
    print( '''

    [*] This program works to encrypt and decrypt texts
        but the decryption key must be available

    [*] Decryption key: It is a number that is specified when creating the encrypted 
        and is given to the second party to be able to decrypt the message

    [*] To ensure that there are no problems
        it is best to use a key with a value less than 10

    [*] If it does not work, try changing the encryption key
    ''')



#===================================

screenClear()
def _lbl():
    screenClear()
    label = '''
    |=================================================================|
    |                                                                 |
    |   This is a program to encode and decode letters and symbols    |
    |                                                                 |
    |   Developed with : Python3                                      |
    |                                                                 |
    |   programmer : Ahmad Nueirat                                    |
    |                                                                 |
    |   github : https://www.github.com/ahmadner                      |
    |                                                                 |
    |=================================================================|
    |                                                                 |
    |    you want:                                                    |
    |                                                                 |
    |   [ 1 ] Encrypt                                                 |
    |   [ 2 ] Decode                                                  |
    |   [ 3 ] Help                                                    |
    |                                                                 |
    |=================================================================|

    '''
    return label

print (_lbl())
do = str(input('     ==> '))

while True:

    if do == '1':
        print (f'\n[+] {_enc()}\n')
        break
    elif do == '2':
        print(f'\n[+] {_unenc()}\n')
        break
    elif do == '3':
        _help()
        break
    else:
        print ('Choose between [1] [2] [3] only')
        do = str(input('==> '))
