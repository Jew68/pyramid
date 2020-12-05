def pyramid(x):
    space = x - 1
    hsh = 1
    for _ in range(x):
        line = []
        for _ in range(space):
            line.append(' ')
        space += -1
        for _ in range(hsh):
            line.append('#')
        hsh += 2
        print (''.join(line))

pyramid(int(input()))
