def remove_rotten(bag_of_fruits):
    if not bag_of_fruits: return []
    return [i if 'rotten' not in i else i[6:].lower() for i in bag_of_fruits]

print(remove_rotten(['rottenBanana', 'apple']))