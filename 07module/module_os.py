import os

print("현재운영체제:", os.name)
print("현재 폴더: ", os.getcwd())
print("현재폴더 내부의 요소:", os.listdir() )

"""os.mkdir("hello")
os.rmdir("hello")

with open("oringnal.txt", "w")as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("new.txt")
"""
os.system("dir")