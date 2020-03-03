def turtle(coord, direction):
    pos = list(coord)
    ways = {0: [1,0], 1: [0,1], 2: [-1,0], 3: [0,-1]}
    step = yield pos
    while step:
        direct = ways[direction]
        if step == 'f':
            pos[0] += direct[0]
            pos[1] += direct[1]
        if step == 'l':
            direction = (direction + 1)%4
        if step == 'r':
            direction = (direction - 1)%4
        step = yield pos
