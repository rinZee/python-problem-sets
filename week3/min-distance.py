


def min_distance(words, word1, word2):
    #Initialize Variables

    w1_index = 0
    w2_index = 0
    # Initialize a variable to store the minimum distance found so far (set to a large number initially).
    minimum_distance = 0
    
    #Iterate Through the List
    for index, word in words:
    #For each word in the list, check if it matches word1 or word2.
    #If the word is word1, record its index.
        if words == word1:
            w1_index = index
    
    #If the word is word2, record its index.
        if words == word2:
            w2_index = index
    
    #Update Minimum Distance
    
    min_distance = w2_index - w1_index
    return min_distance

    #Every time you find a valid index for both word1 and word2, compute the absolute difference between their indices.

    #If this distance is smaller than the current minimum, update the minimum.

    #Return Result

    #After going through the whole list, return the smallest distance found.
    
    


words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)