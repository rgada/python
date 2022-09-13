#"aaAcbBadEF" -> "acadEF"
# 1. consecutive
# 2. similar char
# 3. change of case: bB, aA, Aa, Bb

str = "aaAcbBadEF"
output = ""

i = 0
l_str = len(str)
while i < l_str:
    c1 = str[i]
    if i < l_str - 2:
        c2 = str[i+1]
        if (c1.islower() and c2.isupper() and c1 == c2.lower()) or (c1.isupper() and c2.islower() and c1.lower() == c2):
            i = i+2
            continue
        else:
            output = output + c1
            i += 1
    else:
        output = output + c1
        i += 1

print(output)