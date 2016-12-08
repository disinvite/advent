import hashlib

def hash(input):
    m = hashlib.md5()
    m.update(input)
    return m.hexdigest()
    
def do_that_thing(key):
    password = ''
    i = 0
    while len(password) < 8:
        x = key + str(i)
        y = hash(x)
        if y[:5] == '00000':
            password += y[5]
            print '{}\t{}'.format(i,y)
        i += 1
    return password
    
def do_that_second_thing(key):
    chars_found = 0
    password = [''] * 8
    i = 0
    while chars_found < 8:
        x = key + str(i)
        y = hash(x)
        if y[:5] == '00000':
            pos = y[5]
            char = y[6]
            i_pos = ord(pos)
            if i_pos >= 48 and i_pos < 56:
                pos = int(pos)
                if password[pos] == '':
                    password[pos] = char
                    chars_found += 1
                    print '{0:16} {1}'.format(i,chars_found)
        i += 1
    return ''.join(password)

if __name__ == '__main__':
    #print do_that_thing('abc')
    #print do_that_thing('abbhdwsy')
    #print do_that_second_thing('abc')
    print do_that_second_thing('abbhdwsy')
