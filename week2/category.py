def count_by_category(items):
    # create empty dict
    counts = {}
    # loop through each tuple
    for category, _ in items:
        # if cat is in dict, increment by 1
        if category in counts:
            counts[category] += 1

        # else add teh cat in dict
        else:
            counts[category] = 1
    #return new dict
    return counts
basket = [('fruits', 'apple'), ('veg', 'carrot'), ('fruits', 'grape')]
print(count_by_category(basket))


