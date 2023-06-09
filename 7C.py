data = input()

i = data.split(',')
i.sort()

print(*i, sep = ',')