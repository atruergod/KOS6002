import random
import matplotlib.pyplot as plt

# Generate 15 random numbers between 1 and 300
random_numbers = [random.randint(1, 300) for _ in range(15)]

# Create a simple line graph
plt.figure(figsize=(10, 6))
plt.plot(random_numbers, marker='o', linestyle='-')
plt.title('15 Random Numbers (1-300)')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()
