n=10
fibo=[1,1]
sum=1/4+1/8
for i in range(3,n):
    fibo.append(fibo[-1]+fibo[-2])
    sum+=fibo[-1]/(2**(i+1))
#print(fibo)
print(sum)
print(1.15**(100))
print(1.024**40)
print(2.718**3)