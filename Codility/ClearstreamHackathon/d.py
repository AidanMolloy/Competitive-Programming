# Imports
import random, string

# Solution
def solution(S: str):
    S = list(S)
    for i, char in enumerate(S):
        other_index = len(S) - i - 1
        other = S[other_index]
        # First we need to check if its a placeholder
        if char == "?":
            if other == "?":
                # If other side is also placeholder, make them both "a"
                S[other_index] = "a"
                S[i] = "a"
            else:
                # If other side isnt placeholdr, make current char equal to it
                S[i] = other
        elif other == "?":  
            # If other side is placeholder, make it equal to current char
            S[other_index] = char
        elif char != other:  
            # If opposite characters do not match, not palindrome
            return "NO"
    # Return Answer
    return "".join(S)


def gen(size):

     return (
         "".join(["?" for x in range(size)])
     )

    #return "sa?ppu?kivi???ppias"

print(solution("?ab??a"))
print(solution("bab??a"))
print(solution("?a?"))
print(solution("aa"))