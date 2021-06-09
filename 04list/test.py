numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output =[[], [], []]
for number in numbers:
    output[0:3,3:6,6:].append(number)

print(output)
