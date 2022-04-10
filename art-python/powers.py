#%%
import math
import matplotlib
from matplotlib import pyplot as plt
from functools import cache, lru_cache
import time



#from rich import print
base = 10**1
bottom=9*base
top=10*base
power=10**6
#@lru_cache(maxsize=2)
def plottimes(base, start,stop,step,log):
    start0=time.time()
    args=range(start,stop,step)
    times=[]
    for power in range(start,stop,step):
        start=time.time()
        base**power
        times.append(time.time()-start)
    span=1000
    for args in range(int(start+span),int(stop-span),step):
        sum=0
        for i in range(args-span,args+span+1):
            sum+=times[i]
        times[args]=sum/(2*i+1)
    print("time is ",time.time()-start0)
    plt.plot(args[span:],times[span:])
    plt.show()


#python power
def pythonpower():
    start=time.time()
    for n in range(bottom,top+1):
        result=n**power
        #print(result)
    print("python -> ",round(time.time()-start,2))
#smart power
def smartpower():
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
def naivepower():
    start=time.time()
    for n in range(bottom,top+1): pass
        #result=1
        #for i in range (0,power):
        #    result = n*result
        #print(result)
    print("naive -> ",round(time.time()-start,2))
def power4():
    zoom=100
    bottom=1
    top=2.38
    times=[]
    args=[]
    for i in range(int(bottom*zoom),int(top*zoom+1)):
        start=time.time()
        n=i/zoom
        power4=n**n**n**n
        times.append(time.time()-start)
        print(n)
        print(power4)
        print(times[-1])
        args.append(n)

plottimes(2,0,10**5,1,0)
#power4()
#plt.plot(args,times)
#plt.show()
# %%
