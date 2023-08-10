#This file has been base64 encoded 50 times - write a script to retrieve the flag. Here is the general process to do this:
#1.read input from the file
#2.use function to decode the file
#3.do process in a loop


import base64

fd =open('b64.txt', 'r')

msg = fd.read()
fd.close()

for i in range(0,50):
    flag = base64.b64decode(msg)
    msg = flag
print(flag)
