#from numpy import bincount


numbers =list(range(1,10))
#print(numbers)

#4a=45+3c+W, a=11+(3c+W+1)/4
#cycle through central number
for i in range(1,6):
    numbers.remove(i)
    #cycle through wing numbers
     
    temp=numbers
    #get distribution for wings
    for distrib in range(2**8):
        #bin=format(distrib,'08b')
        #print(bin)
        W=[]
        C=[]
        res = [int(x) for x in str(format(distrib,'08b'))]
        #get 4 numbers distrib
        if res.count(1)==4:
            for j in range(len(res)):
                if res[j]:
                    W.append(numbers[j])
                elif res[j]==0:
                    C.append(numbers[j])
            #print(W)
            s=11+(3*i+sum(W)+1)//4
            if (3*i+sum(W)+1)%4==0:
                #transpositions of W
                print(W)
                W1=[]
                for j in range(4):
                    Wtemp=W
                    W1.append(Wtemp.pop(j))
                    for k in range(3):
                        W1.append(Wtemp.pop(k))
                        #for l in range(2):
                        #    W1.append(W[l])
                        #    W.pop(l)
                        #    W1.append(W[0])
                        #    W=[]

                
                print(s,i,W1,C)
            C=[]
            W=[]

        
        
        #W.append(a)
       
    #res = [int(x) for x in str(num)]
    numbers.append(i)
