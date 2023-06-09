id = input()

c_name = id.replace('@', '.').split('.')

print(c_name[-2])