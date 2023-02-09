numbers = [2,3,4,5,"text"] #mutable 

for juicy in numbers:
    print(juicy)

numbers[0] = 10

print(numbers)

numbers.pop(0)

print(numbers)