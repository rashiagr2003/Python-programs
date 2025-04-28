single_quotes='Hello'
double_quotes="World"
triple_quotes='''!'''
# # Accessing char

print(single_quotes[1])
#  Slicing the char
print(double_quotes[:4])

# Negative indexing
print(single_quotes[-1])
# String concatenation
print(single_quotes[:4]+" "+double_quotes[:5]+triple_quotes[:1])
# String Repetition
print((single_quotes + " " )* 3)
# Lenght of String
print(len(single_quotes))
# Checking Substrings

# substring - string which is the part of main string
# "Hello World" --> "World"

x= single_quotes + double_quotes
print(single_quotes in x)
# String Method/Functions
y= double_quotes.lower()
print(y)
print(single_quotes.upper())
# join,strip,split,replace
print(single_quotes.join("Nukul ashi"))
print(single_quotes.strip('o'))
# Sring formatting-F string
print(f'elcome with {single_quotes}')
print(single_quotes[::-1])
