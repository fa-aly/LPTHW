from socket import fromshare


formatter = "{} {} {} {}"
print(formatter.formate(1, 2, 3, 4))
print(formatter.formate("one", "two", "three", "four"))
print(formatter.formate(True, False, False, True))
print(formatter.formate(formatter , formatter, formatter, formatter))
print(formatter.formate("`Try your", "Own tex here", "Maybe a poem", "Or a song about fear"))
 