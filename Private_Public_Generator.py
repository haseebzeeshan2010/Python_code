import time

a = 7
b = 13
a1 = 5
b1 = 11
privatekey = []
publickey = []

M = (a*b)-1
e = (a1 * M)+ a

d = (b1*M) + b
n = ((e*d)-1)/M

#Printing
print("Generating Public Key...")
time.sleep(1)
publickey.append(e)
publickey.append(n)
print(publickey)
print()

time.sleep(0.5)
print("Generating Private Key...")
time.sleep(1)
privatekey.append(d)

privatekey.append(n)
print(privatekey)

