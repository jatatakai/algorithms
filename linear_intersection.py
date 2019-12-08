import sys
reader = (line.strip() for line in sys.stdin)

for i in range(int(input())):
    n_up = int(next(reader))

    consts_up = [int(x) for x in next(reader).split()]
    n_down = int(next(reader))
    consts_down = [int(x) for x in next(reader).split()]
    pairs = 0
    for i in consts_up:
        for j in consts_down:
            if abs(i - j) % 2 == 0:
                pairs += 1
    print(pairs)
