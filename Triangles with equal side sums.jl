#default top=46 for less than a second vanilla julia computation
top=196
bottom=6
scope=top-bottom+1
timestart=time();
figures=Array{Int32}(undef,scope)

for side=bottom:top
    figures[side-bottom+1]=0
    for i=0:floor(side/3)
        for j=i+1:floor((side-i)/2)
            for k=j+1:side-i-j-1
                #list=[i,j,k,side-i-j,side-j-k,side-k-i]
                #if count(q->(q==i),list)*count(q->(q==j),list)*count(q->(q==k),list)<2
                a=side-i-j
                b=side-j-k
                c=side-j-i
                if a!=i&&a!=j&&a!=k&&b!=i&&b!=j&&b!=k&&c!=i&&c!=j&&c!=k
                    figures[side-bottom+1]+=1
                end
            end  
        end
    end
    #println(side," -> ",figures[side-bottom+1])
end
println(top," -> ",figures[top-bottom+1])
timeend=time()
deltatime=timeend-timestart
println("Calculation took ",deltatime," seconds")
                
                          
