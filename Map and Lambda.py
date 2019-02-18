cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        ret = [0,1]
        for i in range(2,int(n)):
            ret.append(ret[i-1]+ret[i-2])
    return ret

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))