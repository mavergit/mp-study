import time
start=time.time()
#print(start)
k=0
for i in range(10**7):
    k+=i
    #print(k)
end=time.time()
time=round(end-start,2)
print(time)
