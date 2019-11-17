import random

for i in range(10):
    print(random.randint(100,500))

#Using List Comprehension
print([random.randint(100,500) for i in range(5)])