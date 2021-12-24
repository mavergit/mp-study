#%%
#%%timeit
import math
import time
import scipy.special

bottom=10**0
top=10**7
power=1

time1=time.time()
leftside=[bottom**power]
rightside=[bottom**power]
#while (rightside[0]!=0):
for k in range(2,power+3):
    rightside.append((bottom+k-1)**power)
    # now rightside[k-1]=k**power
    #print(k,rightside)
    for i in range(2,k+1):
        rightside[k-i]=rightside[k-i+1]-rightside[k-i]
    leftside.append(rightside[0])
    #print(rightside)
#print(leftside)

sum=0
for i in range(0,power+2):
    sum+=leftside[i]*scipy.special.binom(top-bottom+1,i+1)
    #print(leftside[i]*scipy.special.binom(top-bottom+1,i+1))
time2=time.time()
print(sum)
print("time ",time2-time1)
#%%
#%%timeit
time3=time.time()

sum=0
for i in range(bottom,top+1):
    sum+=i**power
time4=time.time()
print(sum)
print("time ",time4-time3)
print("binomial speedup is ", (time4-time3)/(time2-time1))
# %%
