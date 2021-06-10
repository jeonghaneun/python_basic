example_dictionary = {
    "keyA": " valueA",
    "keyB": " valueB",
    "keyC": " valueC",
    
}

print("#딕셔너리의 item()함수")
print("Items():", example_dictionary.items())
print()

print("딕셔너리의 items()함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dicrionary[{}] = {}".format(key, element))