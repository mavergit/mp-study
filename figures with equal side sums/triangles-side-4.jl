#default top<=100 for less than a second vanilla julia computation
using Plots; gr()
    top=53
    bottom=13
    scope=top-bottom+1
    timestart=time();
    figures=Array{Int}(undef,scope)
    for side::Int=bottom:top
        figures[side-bottom+1]=0
        #println(side)
        for c1::Int=0:floor(side/3)+1
            for c2::Int=c1+1:floor((side-c1)/2)+1
                for c3::Int=c2+1:side-c2-1
                    #local corner=c1+c2+c3

                    local mid1=side-c3-c2
                    local mid2=side-c1-c3
                    local mid3=side-c2-c1
                    for mid11::Int=0:floor(mid1/2)
                        mid12=mid1-mid11
                        for mid21::Int=0:floor(mid2/2)
                            mid22=mid2-mid21
                            for mid31::Int=0:floor(mid3/2)
                                mid32=mid3-mid31
                                triangle=[c1,c2,c3,mid11,mid12,mid21,mid22,mid31,mid32]
                                
                                #sort!(triangle)
                                #println(triangle)
                                count=size(triangle,1)
                                local diff::Int=1
                                for i::Int=1:count-1
                                    for j::Int=i+1:count
                                        if triangle[i]==triangle[j]
                                            diff+=1
                                        
                                        end
                                    end
                                end
                                if diff==1
                                    figures[side-bottom+1]+=1
                                    #println(triangle)
                                end
                            end
                        end
                    
                        #if c1!=m31
                        #if k-i!=side-corner&&k-j!=side-corner&&j-i!=side-corner
                        #figures[side-bottom+1]+=1
                        #println(i,j,k,a,b,c)
                    end
                end  
            end
        end
        println(side," -> ",figures[side-bottom+1])
    end
    #println(top," -> ",figures[top-bottom+1])
    x=bottom:top
   
    lnfigures=Array{Float16}(undef,scope)
    for i=1:scope
        lnfigures[i]=log(figures[i])
    end
    plot1=plot(x,[lnfigures,x])
    #display(plot1)
    #savefig(plot1)
    #display(plot(x,[figures))

    timeend=time()
    deltatime=timeend-timestart
    println("Calculation took ",deltatime," seconds")
                    
                              
    