def wellbracketed(s):
  depth = 0
  
  for i in range(len(s)):
    if s[i] == '(':
        depth = depth + 1
    elif s[i] == ')':
        depth = depth - 1
    print(depth)
    if depth < 0:
        return False
    elif depth == 0:
        return True
    else:
        return False

s = input()
display = wellbracketed(s)
print(display)