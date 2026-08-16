def analyze_text(text):
    words = text.lower().split()

    counts = {}

    total_words = len(words)
    most_common_words = ""

    for word in words:
        if word in counts:
            counts[word] += 1

        else:
            counts[word] = 1

    unique_words = len(counts)
    
    highest_count = 0
    for word in counts:
        if counts[word] > highest_count:
            highest_count = counts[word]

    for word in counts:
        if counts[word] == highest_count:
            most_common_words = word

    return{"total_words": total_words,
            "unique_words": unique_words,
            "most_common_word": most_common_words}
    # return None

result = analyze_text(
    "Python is easy and Python is powerful"
)


print(result)