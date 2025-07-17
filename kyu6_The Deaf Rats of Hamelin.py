def count_deaf_rats(town):
    town = town.replace(" ", "")
    p_index = town.find("P")
    
    left_side = town[:p_index]
    right_side = town[p_index+1:]
    
    def chunk_rats(rats_str):
        return [rats_str[i:i+2] for i in range(0, len(rats_str), 2)]
    
    deaf_left = chunk_rats(left_side).count("O~")
    deaf_right = chunk_rats(right_side).count("~O")
    
    return deaf_right+deaf_left

print(count_deaf_rats("~O~O~O~OP~O~OO~"))