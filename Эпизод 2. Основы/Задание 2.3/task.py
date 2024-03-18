# todo: replace this with an actual task
def task_1(str):
    # TODO
    words = str.split(" ")
    last_word = words[-1]
    length = len(last_word)
    return length


def task_2(str):
    # TODO
    words = str.split()
    swap_words = []

    for i in range(len(words)):
        if i % 2 == 0:
            if i + 1 < len(words):
                swap_words.append(words[i + 1])
            swap_words.append(words[i])

    return ' '.join(swap_words)


def task_3(str):
    # TODO
    words = str.split()
    c = 0

    prev_word = ""
    for word in words:
        if prev_word and word[0].lower() == prev_word[-1].lower():
            c += 1
        prev_word = word
    return c
