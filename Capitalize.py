def solve(s):
    names = s.split()
    return " ".join([name[0].upper()+name[1:] for name in names])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()