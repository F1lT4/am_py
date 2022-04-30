class MyIterator:
    def __init__(self, stop):
        self.stop = stop
        self.step = 0

    def __iter__(self):
        self.n = [1]
        return self

    def __next__(self):
        if 0 == self.step < self.stop:
            self.n.append(self.n[self.step])
            self.step += 1
            return self.n[self.step]
        elif self.step < self.stop:
            self.n.append(self.n[self.step]+self.n[self.step-1])
            self.step += 1
            return self.n[self.step]
        else:
            raise StopIteration


it = MyIterator(100)
for i in it:
    print(i)
