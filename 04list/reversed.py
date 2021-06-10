list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)#뒤집는함수

print("# resersed() 함수 ")
print("reversed([1,2,3,4,5]):", list_reversed)#why?
print("list(reversed([1,2,3,4,5]))", list(list_reversed))
print()

print("#reversed() 함수와반복문")
print("for i in resersed([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-", i)
