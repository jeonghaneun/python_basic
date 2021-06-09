dictionary = {
    "name" : "coffee",
    "type" : "sweet",
    "ingredient": ["been,water"],
    "origin": "kenya"

}

key = input(">접근하고자 하는 키:")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지않습니다.")