"""
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

def one_away(s1, s2):
    """
    Check if a string is one edit away from another
    Input:
        s1 (str): string to check
        s2 (str): string to check
    Return:
        bool: True if one edit away, else false
    """
    n1 = len(s1)
    n2 = len(s2)

    if not (n1 - n2) <= 1:
        return False
    
    