s = input()
s1 = ''
print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))
for i in range(len(s)):
    if (65 <= ord(s[i]) <= 87) or (97 <= ord(s[i]) <= 119):
        s1 += chr(ord(s[i]) + 3)
    elif (88 <= ord(s[i]) <= 90) or (120 <= ord(s[i]) <= 122):
        s1 += chr(ord(s[i]) - 23)
    else:
        s1 += s[i]
print(s1)