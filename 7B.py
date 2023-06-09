line = input()

line = line.split(' ', 1)

data = line[1].split(' ')

for i in range(int(line[0])):
    print(data[i].upper(), end = " ")