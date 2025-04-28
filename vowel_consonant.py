def count(str):
    c1=0
    c2=0
    str=str.lower()
    for i in range(len(str)):
        x=str[i]
        if(x=='a'or x=='e' or x=='i' or x=='o' or x=='u'):
            c1+=1
        
        elif x.isalpha() and x not in 'aeiou':
            c2+=1
       
        else:
            print('Not a alphebet')

    print(f'vowels are {c1}')
    print(f'consonants are {c2}')

def main():
    count('World')
   

main()