string = input().split("\\")

name, extension = string[-1].split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")
