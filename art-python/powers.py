#%%
import math
from rich import print
import time
base = 10**1
bottom=9*base
top=10*base
power=10*4



#python power
start=time.time()
for n in range(bottom,top+1):
    result=n**power
    #print(result)
print("python -> ",round(time.time()-start,2))

#smart power
start=time.time()
for n in range(bottom,top+1):
    multiplier=n
    result=1
    quotient=power
    #powers2=[]
    while quotient>1:
        remainder=quotient-2*int(quotient/2)
        quotient=int(quotient/2)
        #print(multiplier)
        if remainder==1:
            result *= multiplier
        multiplier=multiplier*multiplier
        #print(remainder)
        #powers2.append(remainder)
    #powers2.append(1)
    #multiplier=multiplier*multiplier 
    #print(multiplier)
    result *= multiplier
    #print(result)
print("smart -> ",round(time.time()-start,2))

#naive power
start=time.time()
for n in range(bottom,top+1):
    result=1
    for i in range (0,power):
        result = n*result
    #print(result)
print("naive -> ",round(time.time()-start,2))
#%%
#get powers of 2
n=2
multiplier=n
n=1
power=5
quotient=power
#   powers2=[]
while quotient>1:
    remainder=quotient-2*int(quotient/2)
    quotient=int(quotient/2)
    #print(multiplier)
    if remainder==1:
        n=n*multiplier
    multiplier=multiplier*multiplier
    #print(remainder)
    #powers2.append(remainder)
#powers2.append(1)
#multiplier=multiplier*multiplier 
#print(multiplier)
n=n*multiplier
#print(powers2)
#print(n)

# %%
