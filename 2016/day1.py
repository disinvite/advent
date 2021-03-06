def final_distance(directions):
    # north, east, south, west
    delta = [(0,-1),(1,0),(0,1),(-1,0)]
    chosen_delta = 0 # we start with north
    pos = [0,0]

    directions = [dir.strip() for dir in directions.split(',')]
    for dir in directions:
        turn_dir = dir[0]
        n_steps = int(dir[1:])
        
        if turn_dir == 'R':
            chosen_delta = (chosen_delta + 1) % 4
        elif turn_dir == 'L':
            chosen_delta = (chosen_delta + 3) % 4
        
        dx,dy = delta[chosen_delta]
        pos[0] += dx * n_steps
        pos[1] += dy * n_steps

    return pos[0],pos[1]

def visited_twice(directions):
    # north, east, south, west
    delta = [(0,-1),(1,0),(0,1),(-1,0)]
    chosen_delta = 0 # we start with north
    pos = [0,0]
    locations = [tuple(pos)]

    directions = [dir.strip() for dir in directions.split(',')]
    for dir in directions:
        turn_dir = dir[0]
        n_steps = int(dir[1:])
        
        if turn_dir == 'R':
            chosen_delta = (chosen_delta + 1) % 4
        elif turn_dir == 'L':
            chosen_delta = (chosen_delta + 3) % 4
        
        dx,dy = delta[chosen_delta]
        
        # each step must be added, not the final destination
        for i in range(n_steps):
            pos[0] += dx
            pos[1] += dy
            locations.append(tuple(pos))

    visited = {}
    for p in locations:
        key = '{},{}'.format(p[0],p[1])
        if key in visited:
            break
        else:
            visited[key] = 1
    
    return p
    
def day1_part1(directions):
    x,y = final_distance(directions)
    print 'DISTANCE: {}'.format(abs(x) + abs(y))
    
def day1_part2(directions):
    x,y = visited_twice(directions)
    print 'DISTANCE: {}'.format(abs(x) + abs(y))
    
if __name__ == '__main__':
    input = 'L3, R1, L4, L1, L2, R4, L3, L3, R2, R3, L5, R1, R3, L4, L1, L2, R2, R1, L4, L4, R2, L5, R3, R2, R1, L1, L2, R2, R2, L1, L1, R2, R1, L3, L5, R4, L3, R3, R3, L5, L190, L4, R4, R51, L4, R5, R5, R2, L1, L3, R1, R4, L3, R1, R3, L5, L4, R2, R5, R2, L1, L5, L1, L1, R78, L3, R2, L3, R5, L2, R2, R4, L1, L4, R1, R185, R3, L4, L1, L1, L3, R4, L4, L1, R5, L5, L1, R5, L1, R2, L5, L2, R4, R3, L2, R3, R1, L3, L5, L4, R3, L2, L4, L5, L4, R1, L1, R5, L2, R4, R2, R3, L1, L1, L4, L3, R4, L3, L5, R2, L5, L1, L1, R2, R3, L5, L3, L2, L1, L4, R4, R4, L2, R3, R1, L2, R1, L2, L2, R3, R3, L1, R4, L5, L3, R4, R4, R1, L2, L5, L3, R1, R4, L2, R5, R4, R2, L5, L3, R4, R1, L1, R5, L3, R1, R5, L2, R1, L5, L2, R2, L2, L3, R3, R3, R1'

    day1_part1('R2, L3')
    day1_part1('R2, R2, R2')
    day1_part1('R5, L5, R5, R3')
    day1_part1(input)
    
    day1_part2('R8, R4, R4, R8')
    day1_part2(input)
    