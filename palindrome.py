def palindrome_func(str):
        x=str[::-1]
        if(x==str):
            print('It is palindrome')
        else:
            print('It is not palindrome')


def main():
        palindrome_func('111')

main()