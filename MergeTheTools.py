def merge_the_tools(string, k):
    for segment in zip(*[iter(string)]*k):
        dic = dict()
        print("".join([dic.setdefault(char,char) for char in segment if char not in dic]))
if __name__ == '__main__':
    s = input()
    k = int(input())
    merge_the_tools(s,k)