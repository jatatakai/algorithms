for i in range(int(input())):
    n, k, d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    print(min(len(set(a[i:i+d])) for i in range(n - d + 1)))