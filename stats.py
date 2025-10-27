def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    a = {}
    for i in text.lower():
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    return a


def sort_on(items):
    return items["num"]


def dict_to_list(dict):
    a = []
    for item in dict:
        a.append({"char": item, "num": dict[item]})
    a.sort(reverse=True, key=sort_on)
    return a
