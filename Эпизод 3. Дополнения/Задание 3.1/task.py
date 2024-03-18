def task_1(text):
    sentences = text[:-1].split('. ')
    result = {}

    for sentence in sentences:
        result[sentence] = len(sentence.split())

    return result


text = 'First sent. Second sent and. Third sent and other.'
print(task_1(text))

#-------------------------

x1,y1,x2,y2 = 2,5,4,9
def task_2(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance
print(task_2(x1, y1, x2, y2))



