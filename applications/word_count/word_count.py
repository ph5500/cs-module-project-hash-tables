def word_count(s):
    string = s.replace('"', '').replace(':', '').replace(';', '').replace(',', '').replace('.', '').replace('-', '').replace('+', '').replace('=', '').replace('/', '').replace(
        "|", '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace('*', '').replace('^', '').replace('&', '').replace('\\', '')
    if string == '':
        return {}
    split = string.lower().split()
    words = {i: split.count(i) for i in split}
    return words
    
    
    
    
    
    # counts = dict()
    # words = str.split(s)
    
    # for word in words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1
    
    # return counts
    
 
        
        
    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    
    