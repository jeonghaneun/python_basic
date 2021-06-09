dictionary = {
    "name" : "coffee",
    "type" : "sweet",
    "ingredient": ["been,water"],
    "origin": "kenya"

}

print("name:", dictionary["name"])
print("type:",dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

#값변경
dictionary["name"] ="latte"
print("name:", dictionary["name"])

dictionary["price"] = 5000
print(dictionary)