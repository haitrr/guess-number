file = open("data1.txt")
answers = []
temp = file.readline()
while temp != "":
    answers.append(int(temp))
    temp = file.readline()
file.close()


def guess(remove, from_index):
    count = 0
    for i in range(0, from_index - remove):
        if answers[i] == 1:
            count += 1
    rate = count / (from_index + 1 - remove)
    if rate < 0.5:
        return 0
    else:
        return 1


def accuracy(remove=7):
    count = 0
    for i in range(remove, len(answers) - 1):
        if guess(remove, i) == answers[i + 1]:
            count += 1
    return count / (len(answers) - remove) * 100


print("Accuracy of guesses : " + str(accuracy(7)))
