def sum_all(start= 0, end = 100, step=1):
    output = 0
    for i in range(start,end +1,step):
        output += i
    return output

print("A:", sum_all(0, 100, 10))
print("A-2:", sum_all(0, 100))
print("A-1:", sum_all(0, 100, 20))
print("B:", sum_all(end=100))
print("C:", sum_all(end=100, step=2))

