import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.replace("\n", " ")
words = words.replace("\t", " ")
words = words.replace("\r", " ")

# TODO: analyze which words can follow other words
words = [w for w in words.split(" ") if w is not ""]
starts = []
d = {}




def to_start(word_grab):
    if word_grab[0].isupper():
        return True
    if word_grab[0] == '"' and word_grab[1].isupper():
        return True
    return False


def to_stop(word_grab):
    if word_grab.endswith(("!", "?", ".")):
        return True
    if word_grab.endswith('"'):
        if word_grab[:-1].endswith(("!", "?", ".")):
            return True
    return False


for index, word_grab in enumerate(words):
    if index < len(words) - 1:
        if to_start(word_grab):
            starts.append(word_grab)
        if word_grab in d.keys():
            d[word_grab].append(words[index + 1])
        else:
            d[word_grab] = [words[index + 1]]

           

for i in range(5):
    selected_word = random.choice(starts) 
    print(selected_word, end=" ")
    while not to_stop(selected_word):
        selected_word = random.choice(d[selected_word])
        print(selected_word, end =" ")
    print()
    print()
    
    
    