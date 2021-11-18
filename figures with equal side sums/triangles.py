# default top<=100 for less than a second vanilla julia computation
import math
import time
timestart=time.time()
top=11
bottom=6
scope=top-bottom+1
#julia figures=Array{Int32}(undef,scope)
figures = []
for side in range(bottom,top+1, 1):
    
    figures.append(0)
    figures[side-bottom]=0
    for i in range(0,math.floor(side/3)+1,1):
        
        for j in range(i+1,math.floor((side-i)/2)+1,1):
            
            for k in range(j+1,side-j,1):
               
                #corner=i+j+k
                a=side-i-j
                b=side-j-k
                c=side-k-i

                triangle=[i,j,k,a,b,c]
                
                if a!=i and a!=j and a!=k and b!=i and b!=j and b!=k and c!=i and c!=j and c!=k:
                #if k-i!=side-corner and k-j!=side-corner and j-i!=side-corner:
                    #print(triangle)

                    figures[side-bottom] += 1
    print(side,"->",figures[side-bottom])
    
print(top,"->",figures[top-bottom])
timeend=time.time()
print(timeend-timestart)
#deltatime=timeend-timestart;
#println("Calculation took ",deltatime," seconds");
                
                          
