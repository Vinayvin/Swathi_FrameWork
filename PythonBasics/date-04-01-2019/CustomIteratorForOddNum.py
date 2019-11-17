class Number:

    def __next__(self,num):
        self.num=num
        self.num += 2
        return self.num

obj=Number()
for i in range(3):
    print(obj.__next__(i))