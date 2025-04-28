try:
    result=10/0
except ZeroDivisionError:
    print("It is the zero division error")

try:
    int("Hello")
except ValueError:
    print("Cannot input string with int method")

# File Handling
# open(File Name, mode)
# mode-read(r),write(w),append(a)


with open('sample.txt','a') as f:
  f.write('\n This is my content')

with open('sample.txt','r') as f:
    print(f.read())