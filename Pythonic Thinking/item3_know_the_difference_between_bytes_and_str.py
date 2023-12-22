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


#This first function takes a bytes or str instance and always returns a str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        value=bytes_or_str.decode('utf-8')
    else:
        value=bytes_or_str
    return value #Instance of str
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

#This second function takes a bytes or str instance and always returns a str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        value=bytes_or_str.decode('utf-8')
    else:
        value=bytes_or_str
    return value #Instance of str
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

# you can add bytes instance to bytes instance and 
# you can add str instance to str instance
# you cannot add bytes instance with str instance
"""This below program will show how you can add bytes instance with bytes instance and str instance with str instance"""
print(b'one' + b' two')
print('one' + ' two')
"""
output
b'one two'
one two
"""

"""This below program shows how you cannot add bytes instance with str instance"""
print(b'one' + ' two')

"""
output will be some form of error
"""

#you can compare bytes instance with bytes instance
#and string instance to string instance
assert b'red' > b'blue'
assert 'red' > 'blue'
"""
you will get no output
"""
# you cannot compare bytes instance with str instance
assert b'red' > ' blue'
"""
your output will be some form of error
"""

#comparing bytes instance and str instance will always result to False
print(b'foo' == 'foo')
"""
Here the output will be false
"""



#The % operator works with format strings for each type, respectively
#pass bytes instance to bytes instance 
print(b'red %s' % b'blue') #output b'red blue'
#pass str instance to str instance
print('red %s' % 'blue') #output b'red blue'
#pass str instance to bytes instance
print(b'red %s' % 'blue') #output python doesn't know what binary text encoding to use
#pass bytes instance to str instance
print('red %s' % b'blue') #output same

#trying to write a binary data in a file with the file opened in write mode can cause an error
with open('data.bin','w') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')
#solution you must use wb mode to write binary data
with open('data.bin','wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

#same thing goes with reading data from files
with open('data.bin','r') as f:
  data=f.read() #output is error
 #solution use rb mode
 with open('data.bin','rb') as f:
  data=f.read()

#String encoding
with open('data.bin','r', encoding='utf-8') as f:
  data=f.read()

#check which encoding is used in your system 
import locale
print(locale.getpreferredencoding())

#read or write binary data with mode like
# rb or wb

  
