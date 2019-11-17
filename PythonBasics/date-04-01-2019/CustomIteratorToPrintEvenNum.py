#pgm to print even number between upto 50 using iterator
class EvenNumner:

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

i=iter(EvenNumner())
for j in range(25):
    print(next(i))

#pgm to print odd number between 1 - 50 using iterator