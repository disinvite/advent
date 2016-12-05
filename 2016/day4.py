def split_code(code):
    square_bracket = code.index('[')
    checksum = code[square_bracket + 1:-1]
    rest = code[:square_bracket]
    sections = rest.split('-')
    sector_id = int(sections[-1])
    letters = sections[0:-1]
    
    return {'name': letters, 'id': sector_id, 'checksum': checksum}

def decode_name(code):
    x = split_code(code)
    chars = [[ord(l) - 97 for l in let] for let in x['name']]
    chars = [[(c + x['id']) % 26 for c in section] for section in chars]
    chars = [''.join([chr(c + 97) for c in section]) for section in chars]

    return ' '.join(chars)
    
def part2_map(code):
    x = split_code(code)
    return (decode_name(code),x['id'])
    
def dict_to_tuple_list(d):
    return [(k,d[k]) for k in d.keys()]
    
def frequency_alphabetical_search(item1,item2):
    if cmp(item1[1],item2[1]) == 0:
        return cmp(item1[0],item2[0]) # smallest letter first
    else:
        return -1 * cmp(item1[1],item2[1]) # biggest number first
    
def validate(code):
    x = split_code(code)
    letter_count = {}
    for section in x['name']:
        for letter in section:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
                
    t = dict_to_tuple_list(letter_count)
    t = sorted(t, cmp=frequency_alphabetical_search)
    computed_checksum = ''.join([i[0] for i in t[:5]])
    return computed_checksum == x['checksum']
    
def read_input(filename):
    with open('input/{}'.format(filename),'r') as f:
        lines = [line.strip() for line in f]
    return lines
        
def get_sector(code):
    x = split_code(code)
    return x['id']
        
if __name__ == '__main__':
    input = read_input('day4')
    #print validate('aaaaa-bbb-z-y-x-123[abxyz]')
    #print validate('a-b-c-d-e-f-g-h-987[abcde]')
    #print validate('not-a-real-room-404[oarel]')
    #print validate('totally-real-room-200[decoy]')
    
    x = [get_sector(code) for code in input if validate(code)]
    print sum(x)
    
    print decode_name('qzmt-zixmtkozy-ivhz-343[whate]')
    
    for name,id in map(part2_map,input):
        if 'north' in name:
            print '{} : {}'.format(name,id)