""" 
                    C STYLE STRING FORMATTTING 
"""
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


"""FIRST PROBLEM WHEN FORMATTING A STRING"""
"""What went wrong when we format a string"""
#swap key and value
formatted2='%s=%2.f' % (value,key)
#Here you will get an error
#swap format string
formatted3='%2.f=%s' %(key,value)


"""SECOND PROBLEM WHEN FORMATTING A STRING"""
"""CASES WHERE STRING FORMATTING BECOMES DIFFICULT"""
pantry=[
    ('avocados',1.25),
    ('bananas',2.5),
    ('cherries',15)
    ]
#making no changes in formatting them into string
for i, (item,count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i,item,count))
#output
"""
#0: avocados   = 1.25
#1: bananas    = 2.50
#2: cherries   = 15.00
"""
#making small changes in the modification of values
#long and complex expression
for i, (item,count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count)))
#output
"""
#1: Avocados   = 1
#2: Bananas    = 2
#3: Cherries   = 15
"""


"""THIRD PROBLEM WHEN FORMATTING A EXPRESSION"""
#if you want to use the same value multiple times you have to repeat it in the right hand side
template='%s loves food. See %s cook.'
name='Max'
formatted=template % (name,name)
print(formatted)
#output
"""
Max loves food. See Max cook.
"""
#solution kind of use title method in this case
formatted=template %(name.title(),name.title())
print(formatted)
#output
"""
Max loves food. See Max cook.
"""



"""FOURTH PROBLEM"""
# USING DICTIONARIES IN FORMATTING EXPRESSIONS
# in single line
soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
print(formatted)

# multiple lines with triple-quotes for clarity
menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '  
            'and our special entree is %(special)s'  
            )
formatted = template % menu
print(formatted)
#  OUTPUT
"""
Today's soup is lentil.
Today's soup is lentil, buy one get two kumamoto oysters, and our special entree is schnitzel
"""





"""
                TILL NOW WE WERE FORMATTING STRINGS IN C SYLE NOW 
                WE WILL USE format build-in and str.format 
                
"""
