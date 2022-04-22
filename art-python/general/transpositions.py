def flatlist(t):
    out = []
    for sublist in t:
        out.extend(sublist)
        print(sublist)
    #return out
flatlist([1,[2,3]])
top=4
nums =list("abc")
mat=[[]]
mat[0].append(nums)
sym=[1,2,3]
for i in range(len(sym)):
    extra=sym[:]
    extra.remove(sym[i])
    #print(extra)
    for j in range(len(sym)):
        trans=[]
        trans=extra[:j]
        trans.append(sym[i])
        trans.append(extra[j:])
        #print((trans))

        



    

