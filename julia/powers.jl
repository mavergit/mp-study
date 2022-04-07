
#from matplotlib import pyplot as plt
#import time
#from rich import print
#using Plots; gr()

zoom=100
bottom=zoom
top=240
scope=(top-bottom)*zoom+1
times=Array{Float16}(undef,scope)
args=Array{Float16}(undef,scope)
for i::Int=bottom:top+1
    start=time()
    n=i/zoom
    power4=n^n^n^n
    stop=time()
    times[i-bottom+1]=(stop-start)

    println(n)
    println(power4)
    println(last(times))
    args[i-bottom+1]=n
end
#plt.plot(args,times)
#plt.show()
# %%
