import math

def get_middle(s):
    return s[(math.ceil(len(s)/2))-1] if(len(s)%2!=0) else f'{s[int(len(s)/2)-1]}{s[int(len(s)/2)]}'


print(get_middle("siclke"))