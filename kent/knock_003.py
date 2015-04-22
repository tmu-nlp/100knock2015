str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

w_list = []
words = str.split()
for w in words:
    if w.endswith(',') or w.endswith('.'):
        w = w[:-1]
    w_list.append(len(w))
    """?"""

print w_list
