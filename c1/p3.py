"""
In python, strings are immutable.

Cannot do this operation in place
"""

def URLify(s):
    """
    Replace all spaces in a string with %20
    Inputs:
        s (str): String to URLify
    Returns:
        str: modified string
    """

    s = s.strip()
    return s.replace(" ", "%20")


if __name__ == "__main__":
    print(URLify("Mr John Smith    "))
    print(URLify("Hello World"))