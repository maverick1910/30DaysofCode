n = int(input())
p = bin(n).replace("0b", "")
r = [int(d) for d in str(p)]
f=0
max=0
for i in r:
    if i == 1:
        f=f+1
        if max < f:
            max=f
    else:
        f = 0

print(max)
