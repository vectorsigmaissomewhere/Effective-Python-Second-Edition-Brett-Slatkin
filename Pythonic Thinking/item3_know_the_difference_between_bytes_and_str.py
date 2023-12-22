a=b'h\x65llo'
print(list(a))
print(a)
"""
OUTPUT
[104, 101, 108, 108, 111]
b'hello'
Here b means binary data
and \x65 means e
so this this first converted into ascii values 
and then a is what prints the original bytes object
"""
#str 
#bytes
#   unicode to binary and binary to unicode
#   encode method of str    decode method which is a method of bytes
#   you can use your own ending in this methods
