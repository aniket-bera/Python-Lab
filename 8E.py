def mid_str(s1):
  p = len(s1)//2
  s2 = s1[p-1:p+2]
  print(s2)

str = input()
p = len(str)

if p >= 7 and p%2 != 0:
    mid_str(str)

else:
    print("Wrong Input!!!")