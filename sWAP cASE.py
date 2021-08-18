def swap_case(s):
    n = ''
    for a in s:
        if a.isupper() == True:
            n+=(a.lower())
        elif a.islower() == True:
            n+=(a.upper())
        elif a.isspace() == True:
            n+=a
        else:
            n+=a
    return n

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)