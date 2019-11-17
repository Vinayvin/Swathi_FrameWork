class Custom_Iter(object):
    def __init__(self, low_range, high_range):
        self.current = low_range
        self.high = high_range

    def __iter__(self):

        return self

    def __next__(self):

        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

c = Custom_Iter(1,10)
for i in c:
    print(i)