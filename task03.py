words = ("apple", "banana", "strawberry", "kiwi")
longest = ""
for word in words:
    if  len(word) > len(longest):
        longest = word
print(longest)