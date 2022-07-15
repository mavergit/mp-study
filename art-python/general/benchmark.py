import time
start=time.time()
#print(start)
k=0
def bench():
    for i in range(10**1):
        k+=i
        #print(k)
ban=[[]]
print(len(ban))    
for i in range(1,3):
    ban.append([i,i+1])
    ban[i].append(2*i)
print(ban)
print(len(ban))
for a in ban:
    print(a)
print([1,2]==[2,3])
end=time.time()
time=round(end-start,2)
print(time)
