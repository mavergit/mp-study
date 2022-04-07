import math
from matplotlib import pyplot as plt


start=100;end=150

percent=[]
percent.append(1)
level03=0
for i in range(start,end+1,1):
    percent.append(round((i//2+1)/i,4))
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            p=j//2+1
            q=(i//j)//2+1
            #print(p*q)
            if p*q/i<percent[-1]:
                percent[-1]=round(p*q/i,3)
    if percent[-1]<0.3:
        level03+=1
#print(percent)
print(level03)
plt.plot(percent)
plt.axhline(y=0.3, color='r', linestyle='-')
plt.axhline(y=0.5, color='g', linestyle='-')
plt.show()
        