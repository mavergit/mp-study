import random
import time
#choose 9 times out of (0,1,2) so that none of some triples are made of one choice

#brute looping
global triples
triples=0
global rows
rows=[]
global totalbads,scope
totalbads=0
scope=3**4
def brute_loop():
    global rows,scope
    for a1 in range(3):
        for a2 in range(3):
            for a3 in range(3):
                for a4 in range(3):
                    for a5 in range(3):
                        for a6 in range(3):
                            for a7 in range(3):
                                for a8 in range(3):
                                    for a9 in range(3):
                                        global triples
                                        list=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
                                        #if check_triples(list)==1:
                                        #triples+=1
                                        if check_triples(list)==0:
                                            for a in range(scope):
                                                rows=[]
                                                ban=[]
                                                for i in range(18):
                                                    rows.append(0)
                                                    ban.append(i)
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

                                                    rows[i]=ban[i]
                                                
                                                                        

    print("good lines 18-26, good matrices total", scope*9750-totalbads)
    print("good lines 18-26, bad matrices",totalbads/(scope*9750))
    print("good lines 18-26, good matrices",1-totalbads/(scope*9750))

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
    
        

#print(triples)
#print(3**8+3**7+3**6+3**5+3**3+3)
#print(3**8+3**7+3**6+3**5+2*3**4+3**3+2*3**2+2*3)
#print(triples/(3**9))
#print(3**9-triples)


def check_cols(rows):
    result=1
    global badcols,totalbads
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
                                #print(i+k*3,i+9+l*3,18+k+l*3,rows[i+k*3],rows[i+9+l*3],rows[18+k+l*3])
                                #break
    totalbads+=badcols
    return result


def run_random():
    for a in range(scope):
        global rows
        #random.seed(time.time_ns())
        rows=[]
        for i in range(27):
            
            rows.append(0)
            rows[-1]=random.randint(0,2)
        #print(rows)
        check_cols(rows)
    print("bad matrices",totalbads/(scope))
    print("good matrices",1-totalbads/(scope))

def special_matrix():
    global rows
    rows=[0,2,1,2,1,0,1,0,2,1,0,2,0,2,1,2,1,0,2,1,0,1,0,2,0,2,1]
    print("number of rows is",len(rows))
    print("number of bad triples in the last 9 rows is", check_triples(rows[18:27]))
    check_cols(rows)
    #print(badcols)
    #print(totalbads)
    
    collection=[[]]
    print(len(collection))
    scope=10**6
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
        #print(ban)
        for i in range(18):
            select=[0,1,2]
            #print(ban[i][1:])
            for k in ban[i][1:]:
                select.remove(k)
            if select==[]:
                break
            #print(select)
            rows[i]=random.sample(select,1)[0]
            #print(rows[i])
            if i<9:
                ban[9+i%3+3*rows[i]].append(i//3)
                #print(ban[9+i%3+3*rows[i]])
        #print(rows)
        #check_cols(rows)
        if check_cols(rows)==1:
            t=0
            for i in range(len(collection)-1):
                if rows==collection[i]:
                    break
                t+=1
                
            if t==len(collection)-1:
                collection.append(rows)
            #print(collection)
    #print(len(collection))
    print(collection)
    print(len(collection)-1,"good matrices","from",scope,"random variations")
    

start=time.time()
#brute_loop()
#run_random()
special_matrix()

print(round(time.time()-start,2),"sec")

