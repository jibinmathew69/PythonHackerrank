def print_full_name(a, b):
    s = "Hello firstname lastname! You just delved into python."
    s = s.replace("firstname",a).replace("lastname",b)
    print(s)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)