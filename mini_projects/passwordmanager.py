#! python3
# passwordmanager.py -an insecure password locker program
import pyperclip
import sys

passwords = {
    'email':'whjkaxajbkjdbjjjjjjjjvk',
    'blog':'hjkjkkghgjg',
    'fb':'bullshit'
}
if len(sys.argv) < 2:
    print('usage python pw.py [account] -copy account passsword')
    sys.exit()

account= sys.argv[1] #first sys arg is the account name
if account in passwords:
 pyperclip.copy(passwords[account])
 print('Password for ' + account + ' copied to clipboard.')
else:
 print('There is no account named ' + account)