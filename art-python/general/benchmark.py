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
    ban.append([i])
    ban[i].append(2*i)
    #ban[i][0]=i

print(ban)
print(len(ban))
if ban[1]==[1,2]:
    ban.append([3,4])
    print(ban)
end=time.time()
time=round(end-start,2)
print(time)
