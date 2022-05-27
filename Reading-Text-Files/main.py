# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

def count_words():
    texts = read_file_content("./story.txt")
    words_count = {}
    texts = texts.split()
    for text in texts:
        if text in words_count:
            words_count[text] += 1
        else:
            words_count[text] = 1
    return words_count
print(count_words())
    # [assignment] Add your code here

    return {"as": 10, "would": 20}