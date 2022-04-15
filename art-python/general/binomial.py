#%%time
import math
#from rich import print

import time
import timeit
import scipy.special

#print("Select power to sum")
#power=int(input())
start_time = timeit.default_timer()
time1=time.time()

top=10**3
bottom=1
row = [1]
temp=[0]
#row.append(1)
#row[0]=1
for k in range(2,top+2):
    
    row.append(1)
    temp.append(0)
#   print(k, row)
    for i in range(1,k-1):
        #print(row[i])
        row[i]=temp[i]+temp[i-1]
    for i in range(0,k ):
        temp[i]=row[i]
#print(row)
elapsed = timeit.default_timer() - start_time
time2=time.time()
print("naive time spent is ",time2-time1)
print("timeit gives time", elapsed)
#%%
#%%time
time3=time.time()
sum=0
temp=[1]
for i in range(1,top+1):
    temp.append(0)
    for k in range(0,i+1):
        temp[k]=scipy.special.binom(i,k)
    #print(temp)
time4=time.time()
#print(top,row)
#print(top,temp)

print("scipy.special.binom time spent is ",time4-time3)
print("speedup is ",(time4-time3)/(time2-time1))



# %%
