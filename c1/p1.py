def unique_char(input):
    '''
    Determine if a string has all unique characters
    Inputs:
        input (str): input string
    Return:
        bool: Whether or not all the characters are unique
    '''
    map = {}
    for i in input:
        if i in map:
            return False
        map[i] = 1
    return True

def unique_char2(input):
    i = 0
    n = len(input)
    while i < n:
        j = i + 1
        while j < n:
            if input[i] == input[j]:
                return False
            j += 1
        i += 1
    return True



if __name__ == "__main__":
    print(unique_char2("abcdef"))
    print(unique_char2("a"))
    print(unique_char2("aafee"))
    print(unique_char2(""))