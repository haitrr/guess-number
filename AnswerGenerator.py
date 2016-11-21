import random

file = open("data1.txt", 'w')
random.seed(1)
for i in range(0, 5000):
    if random.randint(0, 100) > 60:
        file.write("1\n")
    else:
        file.write("0\n")
file.close()
