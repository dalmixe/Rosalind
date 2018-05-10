j = 1
s = 0
time_to_wait = 81
grow = 1
lifetime = 19
newborns = {}
for z in range (1-lifetime,0):
    newborns[z]=0
newborns[0]=1
j_now = 1

for i in range(1,time_to_wait):
    j_now = j
    j = grow*s
    newborns[i] = j
    s = j_now + s - newborns[i-lifetime]
    #s, j = j + s, grow * s

print(j+s)