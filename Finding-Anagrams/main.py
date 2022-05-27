# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(w1, w2):
    if(sorted(w1)== sorted(w2)):
        return True
    else:
        return False

w1 = "listen"
w2 = "silent"
print(find_anagrams(w1, w2))

