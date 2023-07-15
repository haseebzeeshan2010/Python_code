'''
                
def SieveOfEratosthenes(n):
    
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            print (p,end=' ') #Use print(p) for python 3
 
# driver program
n = int(input("Enter a max number of prime numbers"))
print ("Following are the prime numbers smaller", end=' ')
#Use print("Following are the prime numbers smaller") for Python 3
print ("than or equal to", n)
#Use print("than or equal to", n) for Python 3
SieveOfEratosthenes(n)     

    
#Le tortoise(me) and le hare(estra-somebody's algorithm)!

import time
#A prime number is only divisible by 1 and itself
#N.B. 1 itself, is not counted as a prime number
start = time.time()
n = int(input("Enter an integer number: "))
prime = [] # An empty list

# create an array containing all the numbers
#up to the input number
for i in range(n+1):  
    prime.append(i)

#prime[0]=0
prime[1]=0

print(prime)

p = 2
while (p * p <= n):    
    # If prime[p] is not changed, then it is a prime     
    # Update all multiples of p to zero
    for i in range(p*2, n+1, p):
        #print()
        #print("p is:",p)
        #print("i is:",i)
        prime[i] = 0
        #print("prime",prime)
        #input()

    p=p+1

#print all element of list which are not zero
print("All the prime numbers up to", n, "are:")
for i in range(len(prime)):
    if (prime[i] != 0):
        print(prime[i], end=" ")

end = time.time()
print("The time of execution of above program is :", end-start)
'''
n = int(input("enter a number above 1 "))
arr = []
primes = []
count = 0
p = 2
if n > 1:
    for i in range(2,n+2):
        arr.append("p")

    for i in range(p**2,n+1,p):
        arr[i] = "n"
        print(arr)

        


'''
import time
6
start = time.time()

max = int(input("enter a number above 1 "))



def check(unchecked,max):
    decider = False
    for i in range(2,unchecked-1):
        if unchecked%i == 0:
            decider = True
            
    if decider == True:
        return(f"{unchecked} is not prime")
    else:
        return(f"{unchecked} is prime")


if max > 1:
    
  for i in range(2,max+1):
      print(check(i,max))
    
end = time.time()

print("The time of execution of above program is :", end-start)'''