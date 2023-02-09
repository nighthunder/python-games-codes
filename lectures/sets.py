unique_immutable_group = {1,2,3,4,4}

print(unique_immutable_group)
print(type(unique_immutable_group))

unique_immutable_group2 = {1,2,3,4,4,"besta"}

print(unique_immutable_group2)
print(type(unique_immutable_group2))

# unique_immutable_group2[0] = 30 # TypeError: 'set' object does not support item assignment
# You have to convert if you need to change a immutable type

short_list = [1,2,2,3,3,4,4,5,5,None,"Tesla"]

short_list = set(short_list)

print(short_list)


