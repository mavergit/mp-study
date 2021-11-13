#default top=46 for less than a second vanilla julia computation
top=46;
bottom=6; scope=top-bottom+1;
timestart=time();
figures=Array{Int32}(undef,scope)

for side in range(bottom,top,step=1)
    figures[side-bottom+1]=0
    for i in range(0,floor(side/3),step=1)
        for j in range(i+1,floor((side-i)/2),step=1)
            for k in range(j+1,side-i-j-1,step=1)
                list=[i,j,k,side-i-j,side-j-k,side-k-i]
                #println(list)
                if count(q->(q==i),list)*count(q->(q==j),list)*count(q->(q==k),list)<2
                    figures[side-bottom+1]+=1
                end
            end  
        end
    end
    #println(side," -> ",figures[side-bottom+1])
end
println(top," -> ",figures[top-bottom+1])
timeend=time();
deltatime=timeend-timestart;
println("Calculation took ",deltatime," seconds");
                
                          
