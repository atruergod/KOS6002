import random
import matplotlib.pyplot as plt
# 숫자 15개 생성
numbers = [] # empty list
for i in range(15):
    print(i)
    random_number = random.randint(1, 100)
    numbers.append(random_number)
    print(i, numbers)

plt.plot(numbers, marker='o')
plt.show()