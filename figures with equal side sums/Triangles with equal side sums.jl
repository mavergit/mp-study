#default top<=100 for less than a second vanilla julia computation
top=96
using Plots; gr()
bottom=6
scope=top-bottom+1
timestart=time();
figures=Array{Int}(undef,scope)
for side::Int=bottom:top
    figures[side-bottom+1]=0
    for i::Int=0:floor(side/2)-1
        for j::Int=i+1:floor(side/2)
            for k::Int=j+1:side-j
                local corner=i+j+k
                local a=side-i-j
                local b=side-j-k
                local c=side-k-i
                if a!=i&&a!=j&&a!=k&&b!=i&&b!=j&&b!=k&&c!=i&&c!=j&&c!=k
                #if k-i!=side-corner&&k-j!=side-corner&&j-i!=side-corner
                    figures[side-bottom+1]+=1
                    #println(i,j,k,a,b,c)
                end
            end  
        end
    end
    #println(side," -> ",figures[side-bottom+1])
end
#println(top," -> ",figures[top-bottom+1])
lnfigures=Array{Float16}(undef,scope)
for i=1:scope
    lnfigures[i]=log(figures[i])
end
x=bottom:top
display(plot(x,figures))
display(plot(x,lnfigures))
plot1=plot(x,[lnfigures,x])
display(plot1)
#savefig(plot1)

timeend=time()
deltatime=timeend-timestart
println("Calculation took ",deltatime," seconds")
                
                          
