from collections import OrderedDict

dic = OrderedDict()
for _ in range(int(input())):
    word = input()
    dic[word] = dic.get(word,0)+1

print(len(dic))
print(*dic.values(),sep=" ")