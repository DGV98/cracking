"""
Tact Coa
output = true (taco cat)
"""

def check_palindrome(s):
    """
    Check if a permutation of letters creates a palindrome
    Input:
        s (str): String to check
    Return:
        bool: Whether or not the string can be rearranged into a palindrome
    """
    s = s.replace(" ", "").lower().strip()
    hashmap = {}
    for i in s:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    letters_odd = 0
    for count in hashmap.values():
        if count%2 != 0:
            letters_odd += 1
    if letters_odd <= 1:
        return True
    return False


if __name__ == "__main__":
    print(check_palindrome("Tact Coa"))
    print(check_palindrome(""))
    print(check_palindrome("Mom    "))
    print(check_palindrome("Mom om"))
    print(check_palindrome("chekc"))