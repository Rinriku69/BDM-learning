#challenge 1
"""words = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "silent"]
group = {}

for i in words:
    s=sorted(i)
    signature = "".join(s)
    #for key in group.keys():
    if signature not in group.keys():
        group[signature] = [i]
    else:
        group[signature].append(i)

print("In group"+"-"*20)
print(group) """

#challenge 2
""" text = "Python is great. Python is easy. Data Mining using Python is powerful. Mining"
lower_text = text.lower()

print(lower_text)

replace_text = lower_text.replace('.','')

print(replace_text)

split_text = replace_text.split()

print(split_text)

word_count={}

for word in split_text:
    if word not in word_count.keys():
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] + 1

split_word_count = word_count.items()
sorted_items = sorted(split_word_count, key=lambda x: x[1], reverse=True)
top_3 = sorted_items[:3]
print(top_3) """





