def mul(*values):
    output = 1
    for value in values:
       output *=value
    return output
print(mul(1,3,4,5,8))