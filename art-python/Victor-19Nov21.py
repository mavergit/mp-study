import time
#print("введите верхнюю границу")
#q=input()
#q=int(q)
q=3
w=1
start=time.time()

a=int(q/2)
a=str((1+q)*a)

end=time.time()
print("сумма от "+str(1)+" до "+str(q)+" = "+a)
print("время", end-start)