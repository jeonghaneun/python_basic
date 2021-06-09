numbers = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,2,4,5,7,8,5,6,7,8,6]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] =counter[number]+1
    else:
        counter[number] = 1

print(counter)