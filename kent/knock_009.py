import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

list = []
words = text.split()
for word in words:
    if len(word) <= 4:
        list.append(word)
    else:
        head = word[0]
        body = word[1:-1]
        tail = word[-1]
        body_list = []
        for char in body:
            body_list.append(char)
        random.shuffle(body_list)
        new_word = "%s%s%s" % (head, "".join(body_list), tail)
        list.append(new_word)
print " ".join(list)
