# def solve(s):
#     names = s.split()
#     return " ".join([name[0].upper()+name[1:] for name in names])
# the above methods compromises on the spacing between the words

import string
def solve(s):
    return string.capwords(s, ' ')



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()