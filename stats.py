def count_words(text):
    words = text.split()
    return len(words)

def character_usage(text):
    usage = {}
    for char in text.lower():
        if char not in usage:
            usage[char] = 1
        else:
            usage[char] += 1

    return usage

def sort_on(item):
    return item["num"]

def get_sorted_usage(usage_dict):
    report = []
    for char, count in usage_dict.items():
        report.append({"char": char, "num": count})

    report.sort(reverse=True, key=sort_on)

    return report
