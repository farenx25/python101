def bus_stop(a):
    z = []
    bus = 1
    for i in range(len(a)):
        z.append(a[i])
        if sum(z) < bus:
            if i == len(a) - 1:
                bus +=1
            else:
                pass
        elif sum(z) == bus:
             if i == len(a) - 1:
                pass
             else:
                 bus +=1
                 z = []
        elif sum(z) > bus:
            if len(z) == 1:
                up = sum(z) - bus
                for k in range(up):
                    bus += 1
                z = []
            else:
                bus +=1
                up = sum(z) - bus
                for k in range(up):
                    bus += 1
                z = []    
    return bus



print(bus_stop([1,2,3]))
print(bus_stop([5]))
print(bus_stop([5,1,1]))
print(bus_stop([5,7]))
