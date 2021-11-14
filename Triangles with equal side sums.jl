#default top<=100 for less than a second vanilla julia computation
top=96
bottom=6
scope=top-bottom+1
timestart=time();
figures=Array{Int}(undef,scope)
for side=bottom:top
    figures[side-bottom+1]=0
    for i=0:floor(side/3)
        for j=i+1:floor((side-i)/2)
            for k=j+1:side-i-j-1
                #local corner=i+j+k
                local a=side-i-j
                local b=side-j-k
                local c=side-k-i
                if a!=i&&a!=j&&a!=k&&b!=i&&b!=j&&b!=k&&c!=i&&c!=j&&c!=k
                #if k-i!=side-corner&&k-j!=side-corner&&j-i!=side-corner
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
                
                          
