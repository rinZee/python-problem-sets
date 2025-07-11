def reverse_only_letters(s):
    #Identify all the letters in the string:
    strings = []
    #Go through the string from left to right.
    for str in s:
    #Extract and store all characters that are letters (e.g., using isalpha() if you were coding).
        if str.isalpha():
            strings.append(str)
    result = ""
    #go through the original string
    for char in s:
        if char.isalpha():
            #add thw last letter fron the list (reversed order)
            result += strings.pop()
        else:
            #keep non letter characters in place
            result += char
            
    return result

    
s = "a-bC-dEf-ghIj"

print(reverse_only_letters(s))