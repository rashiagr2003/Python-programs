# Creating tuple
my_tuple=(1, 2, 3)
print(my_tuple)
# Acessing element
print(my_tuple[2])
#  merging
tp=('a','b','c')
tp1=(1,4,3)
print(my_tuple+tp)
print(my_tuple*4)
# tuple unpacking
a,b,c=(12,4,6)
print(a)
# List-muttable (add, remove, modify), more memory
# Tuple- immutable(can't), less memory

# Sets-contain unique value
ls=[1,4,7,9,4,7]
r=set(ls)
print(r)

#  Set Operation
s1={1,4,3}
s2={2,4,8}
print(s1.union(s2))
print(s1.intersection(s2))