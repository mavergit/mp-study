#%%
# default top<=100 for less than a second vanilla julia computation
import math
from matplotlib import pyplot
#from rich import print
import time
timestart=time.time()
top=96
bottom=6
scope=top-bottom+1
figures = []
xargs=[]
for side in range(bottom,top+1):
    xargs.append(side)
    figures.append(0)
    #figures[side-bottom]=0
    for i in range(0,math.floor(side/2),1):
        
        for j in range(i+1,math.floor(side/2)+1):
            a=side-i-j
            #if a!=i and a!=j:
            if 2*i+j==side or 2*j+i==side:
                continue
            
            for k in range(j+1,side-j+1):
                #corner=i+j+k 
                b=side-j-k
                c=side-k-i                           
                #triangle=[i,j,k,a,b,c]
                if a!=k and b!=i and b!=j and b!=k and c!=i and c!=j and c!=k:
                    #continue

                #print(triangle)
                    figures[side-bottom] += 1
    #print(side,"->",figures[side-bottom])
    
#print(top,"->",figures[top-bottom])

logfigures=[]
yargs=[]
for i in range(len(figures)):
    logfigures.append(math.log(figures[i]))
    yargs.append(3*math.log(xargs[i]))
pyplot.plot(xargs,logfigures)
pyplot.plot(xargs,yargs)
pyplot.show()
print("time for calculation", round(time.time()-timestart,2))

                
                          

# %%
