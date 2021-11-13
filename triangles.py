# default top=46 for less than a second vanilla julia computation
import math
import time
timestart=time.time()
top=196
bottom=6
scope=top-bottom+1
#julia figures=Array{Int32}(undef,scope)
figures = []
for side in range(bottom,top+1, 1):
    
    figures.append(0)
    figures[side-bottom]=0
    for i in range(0,math.floor(side/3),1):
        
        for j in range(i+1,math.floor((side-i)/2),1):
            
            for k in range(j+1,side-i-j,1):
               
                #triangle=[i,j,k,side-i-j,side-j-k,side-k-i]
                #print(triangle)
                #if triangle.count(i)*triangle.count(j)*triangle.count(k)<2:
                a=side-i-j
                b=side-j-k
                c=side-j-i
                if a!=i and a!=j and a!=k and b!=i and b!=j and b!=k and c!=i and c!=j and c!=k:
                    figures[side-bottom] += 1
    #print(side,"->",figures[side-bottom])
    
print(top,"->",figures[top-bottom])
timeend=time.time()
print(timeend-timestart)
#deltatime=timeend-timestart;
#println("Calculation took ",deltatime," seconds");
                
                          
