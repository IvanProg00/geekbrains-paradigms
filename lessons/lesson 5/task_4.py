import re


def popularity(s: str):
    data = {}

    for w in re.split("[ ,.]", s):
        if w != "":
            w = w.lower()
            val = data.get(w, 0)
            data[w] = val + 1

    return sorted(data.items(), key=lambda x: x[1], reverse=True)


print(popularity("Hello world. Hello Python"))
