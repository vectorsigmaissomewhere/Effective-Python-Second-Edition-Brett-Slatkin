#Use % to convert binary values and hexadecimal values to integer strings
a=0b10111011
b=0xc5f
print('Binary is %d, hex is %d' %(a,b)) 
#output Binary is 187, hex is 3167

"""Formatting a string"""
key='my_var'
value=1.234
formatted='%-10s =%.2f' % (key,value)
print(formatted)
#output my_var     =1.23
formatted1='%s=%2.f' % (key,value)
print(formatted1)
#output my_var= 1

"""What went wrong when we format a string"""
#swap key and value
formatted2='%s=%2.f' % (value,key)
#Here you will get an error
#swap format string
formatted3='%2.f=%s' %(key,value)
