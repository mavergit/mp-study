import random
import time
#choose 9 times out of (0,1,2) so that none of some triples are made of one choice

global rows
rows=[]
global totalbads,scope
totalbads=0
scope=3*10**2
def brute_loop():
    base9=0;good9=0
    collection=[[]]
    for a1 in range(3):
        for a2 in range(3):
            for a3 in range(3):
                for a4 in range(3):
                    for a5 in range(3):
                        for a6 in range(3):
                            for a7 in range(3):
                                for a8 in range(3):
                                    for a9 in range(3):
                                        list=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
                                        if check_triples(list)==0:
                                            base9+=1
                                            delta=0
                                            for a in range(scope):
                                                ban=[[0]]
                                                rows=[0]
                                                for i in range(1,18):
                                                    ban.append([i])
                                                    rows.append(0)
                                                rows.extend(list)
                                                for l in range(3):
                                                    for k in range(3):
                                                        for i in range(3):
                                                            b3=rows[18+k+l*3]-i
                                                            if b3==0:
                                                                ban[i+k*3].append(b3+l)
                                                                ban[9+i+l*3].append(b3+k)                                                
                                                for i in range(18):
                                                    select=[0,1,2]
                                                    for k in ban[i][1:]:
                                                        select.remove(k)
                                                    if select==[]:
                                                        break
                                                    rows[i]=random.sample(select,1)[0]
                                                    if i<9:
                                                        ban[9+i%3+3*rows[i]].append(i//3)
                                                if check_cols(rows)==1:
                                                    t=0
                                                    for i in range(1,len(collection)):
                                                        if rows==collection[i]:
                                                            break
                                                        t+=1
                                                    if t==len(collection)-1:
                                                        new=rows[:]
                                                        collection.append(new)
                                                        delta+=1
                                            num=len(collection)-1
                                            if delta!=0:
                                                good9+=1
    print(len(collection)-1,"good matrices","from",scope,"educated random variations for",good9,"good last 9 rows" )
                                                
def check_triples(list):
    result=0
    if (list[0]==list[1]==list[2]):
        result=1
    elif (list[3]==list[4]==list[5]):
        result=1
    elif (list[6]==list[7]==list[8]):
        result=1
    elif (list[0]==list[3]==list[6]):
        result=1
    elif (list[7]==list[1]==list[4]):
        result=1
    elif (list[5]==list[8]==list[2]):
        result=1
    return result
    
def check_cols(rows):
    result=1
    badcols=0
    for l in range(3):
        if badcols==0:
            for k in range(3):
                if badcols==0:
                    for i in range(3):
                        if badcols==0:
                            b1=rows[i+k*3]-l
                            b2=rows[9+i+l*3]-k
                            b3=rows[18+k+l*3]-i
                            if (b1==b2==0 or b2==b3==0 or b3==b1==0):
                                badcols+=1
                                result=0
    totalbads+=badcols
    return result

def special_matrix():
#    global rows
    rows=[0,2,1,2,1,0,1,0,2,1,0,2,0,2,1,2,1,0,2,1,0,1,0,2,0,2,1]
    print(rows,'\n')
    check_cols(rows)
    collect_rows=[[]]
    for a in range(scope):
        ban=[[0]]
        for i in range(1,18):
            ban.append([i])
        for l in range(3):
                for k in range(3):
                        for i in range(3):
                            b3=rows[18+k+l*3]-i
                            if b3==0:
                                ban[i+k*3].append(b3+l)
                                ban[9+i+l*3].append(b3+k)
        for i in range(18):
            select=[0,1,2]
            for k in ban[i][1:]:
                select.remove(k)
            if select==[]:
                break
            rows[i]=random.sample(select,1)[0]
            if i<9:
                ban[9+i%3+3*rows[i]].append(i//3)
        if check_cols(rows)==1:
            for i in range(1,len(collect_rows)):
                if rows==collect_rows[i]:
                    break
                t+=1    
            if t==len(collect_rows)-1:
                new=rows[:]
                collect_rows.append(new)
    print(collect_rows)
    print(len(collect_rows)-1,"good matrices","from",scope,"educated random variations")
    
for i in range(1,2):
    start=time.time()
    brute_loop()
    #special_matrix()
    print(round(time.time()-start,2),"sec")

