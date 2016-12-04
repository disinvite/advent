def possible_triangle(sides):
    tests = [
        (sides[0] + sides[1]) > sides[2],
        (sides[0] + sides[2]) > sides[1],
        (sides[1] + sides[2]) > sides[0]
    ]
    return all(tests)

def col_triplet(cube):
    return [[cube[0][0],cube[1][0],cube[2][0]], [cube[0][1],cube[1][1],cube[2][1]], [cube[0][2],cube[1][2],cube[2][2]]]
    
def read_input(filename):
    with open('input/{}'.format(filename),'r') as f:
        lines = [line.strip() for line in f]
    return lines
        
if __name__ == '__main__':
    #print possible_triangle('5 10 15')
    #print possible_triangle('3 4 5')

    input = [[int(x) for x in y.split()] for y in read_input('day3')]
    result = [i for i in input if possible_triangle(i)]
    print len(result)
    
    modified_input = []
    for i in range(0,len(input),3):
        modified_input += col_triplet(input[i:i+3])
        
    modified_result = [i for i in modified_input if possible_triangle(i)]
    print len(modified_result)
