L1 = [1, 2, 2, 3, 2, 3, 4, 5]

L1.sort()

current=None
curr_count=0
max_count=0
rep=None
for num in L1:
    if num==current:
        curr_count+=1
    else:
        current=num
        curr_count=1
    if curr_count>max_count:
            max_count=curr_count
            rep=current

print(f'num {rep} appears {max_count} times')