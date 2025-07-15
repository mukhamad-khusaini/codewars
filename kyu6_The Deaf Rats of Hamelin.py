def count_deaf_rats(town):
    town = town.replace(" ", "")
    p_index = town.find("P")
    
    left_side = town[:p_index]
    right_side = town[p_index+1:]
    
    def chunk_rats(rats_str):
        return [rats_str[i:i+2] for i in range(0, len(rats_str), 2)]
    
    deaf_left = [rat for rat in chunk_rats(left_side) if rat == "~O"]
    deaf_right = [rat for rat in chunk_rats(right_side) if rat == "O~"]
    
    return len(deaf_left) + len(deaf_right)