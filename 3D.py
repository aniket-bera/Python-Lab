c = input("Enter a character --> ")

if c >= "A" and c <= "Z":
    print("{} is an uppercase character.".format(c));

elif c >= "a" and c <= "z":
    print("{} is a lowercase character.".format(c));

else:
    print("{} is not an aplhabetic character.".format(c));