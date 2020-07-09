# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
with open('ciphertext.txt', 'r') as f:

f = open('ciphertext.txt', 'r')

content = f.read()
# Your code here
def encode(s):
    r = ""
    
    for c in s:
        r += [c]
    return r 

print(encode(f.mode))

