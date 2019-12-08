def build_roof(n, planks):
    '''Function takes the input, assigns every plank size its amount, then finds max_size, linear time'''
    planks.sort(reverse=True)
    sizes = list(set(planks))
    sizes.sort(reverse=True)
    amount = {}
    max_size = 0

    for i in sizes:
        amount[i] = planks.count(i)
        width = sum([amount[j] for j in sizes if j >= i])
        if i < width:
            if max_size < i:
                max_size = i
        else:
            if max_size < width:
                max_size = width
    print(max_size)

if __name__ == '__main__':
    for i in range(int(input())):
        build_roof(int(input()), list(map(int, input().split())))
