list_a = [0, 1, 2, 3, 4, 5]
print("#리스트의 요소하나 제거하기")
print(list_a)

del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2)
print("pop(2):", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]
print("#리스트 [3:6]제거시")
print(list_b)

del list_b[3:6]
print(list_b)

print("#리스트값지정제거")
list_c = [0, 1, 2, 3, 4, 5, 6]
print(list_c)
list_c.remove(2)
print("list_c.remove(2)")
print(list_c)

