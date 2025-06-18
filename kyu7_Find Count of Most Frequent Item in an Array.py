import statistics
def most_frequent_item_count(collection):
    return collection.count(statistics.mode(collection)) if collection else 0