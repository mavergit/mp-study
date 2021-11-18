import math
import time
import timeit
import scipy.special


#print("Select power to sum")
#power=int(input())
time1=time.time()
power=2
top=10**1
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
time2=time.time()
print(top,row)
print("Time spent is ",time2-time1)


