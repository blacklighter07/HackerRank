if __name__ == '__main__':
    n = int(input())
    arr = map(int,input().split())
    
    ar = list(set(arr))
    ar.sort()
    print(ar[-2])
    
