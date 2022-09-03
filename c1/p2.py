"""
abc -> cba
"""

def check_permutation(s1, s2):
    '''
    Method to check if one string is a permutation of the other
    Inputs:
        s1 (str): String 1
        s2 (str): String 2
    Return:
        bool: Whether or not they are a permutation of each other
    '''
    n1 = len(s1)
    n2 = len(s2)

    if n1 != n2:
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    return False

def check_permutation2(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        return False

    hashmap = {}
    for i in s1:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for j in s2:
        if j in hashmap:
            hashmap[j] -= 1
            if hashmap[j] < 0:
                return False
        else:
            return False
    return True


if __name__ == "__main__":
    print(check_permutation2("abc", "bac"))
    print(check_permutation2("", ""))
    print(check_permutation2("lol", "lmfao"))
    print(check_permutation2(",lol", "o,ll"))
