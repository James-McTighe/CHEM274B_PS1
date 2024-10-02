def hash(input_list):
    
    output_dict = {}
    
    for i in input_list:
        h = (10 * i + 4) % 7
        output_dict.update({i:h})

    return output_dict

def hash2(input_list):
    
    output_dict = {}
    c = 13
    for i in input_list:
        h = ((10 * i + 4) % c) % 7
        print(h)
        
        output_dict.update({i:h})

    return output_dict

def hash3(input_list):

    output_dict = {}

    for x in input_list:
        h = x % 10
        output_dict.update({x:h})

    return output_dict

x = [3441,3412,498,1983,4893,3874,3722,3313,4830,2001,3202,365,128181,7812,1299,999,18267]

y = hash3(x)

for _ in y:
    print(_, y[_])