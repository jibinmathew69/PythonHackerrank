data = list(input())
lower = sorted(filter(lambda x:x.islower(), data))
upper = sorted(filter(lambda x:x.isupper(), data))
odd = sorted(filter(lambda x:x.isdigit() and int(x)%2!=0, data))
even = sorted(filter(lambda x:x.isdigit() and int(x)%2==0, data))

print("".join(lower),"".join(upper),"".join(odd),"".join(even),sep="")