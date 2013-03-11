from itertools import product

l = [ 41, 61, 142, 261, 495, 980 ]

a = [x for x in product('01', repeat=6)]

delays = []
for bits in a:
    tot = 0
    for i,x in enumerate(bits):
        x = int(x)
        tot += x*l[i]
    delays.append(tot)

delays.sort()
old = -41 
min = 100
for delay in delays:
    print delay,
    print delay - old
    if (delay - old) < min:
        min = delay-old
    old = delay
print min
