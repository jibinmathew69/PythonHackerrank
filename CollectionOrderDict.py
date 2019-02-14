from collections import OrderedDict

dic = OrderedDict()

for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    dic[item] = dic.get(item,0)+int(quantity)

for key,value in dic.items():
    print("%s %s"%(key,value))