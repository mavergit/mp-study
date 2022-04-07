seats=3

num=0
for i in range(1,seats):
    a=[]
    a.append(1)
    for j in range(1,seats):
        for k in range (2,seats+1):
            b=[]
            b.append(k%seats)
            end=0
            
            for t in range(seats*1+1):
                
                a.append((a[-1]+i)%seats)
                if a[-1]==b[-1]:
                    end=1
                    break
                b.append((b[-1]+j)%seats)
                if a[-1]==b[-1]:
                    end=1
                    break
            
            if end==0:
                num+=1
                print(i,j,"infinity")
                break
            elif end==1:
                print(a)
                print(b)
                print("-")
print(num)