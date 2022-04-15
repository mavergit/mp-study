import time
sum=0
bottom=1
top=10**3
start=time.time()
#for k in range(bottom,top+1):
#    #print(k)
#    sum+=k
sum=(top-bottom+1)*(top+bottom)/2    
end=time.time()
print(sum)
print("Time for ",bottom," to ",top," is ",end-start)
    