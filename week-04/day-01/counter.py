class Counter(object):
    def __init__(self, number=0):
        self.number = number

    def add(self, number = 1):
        self.number += number

    def reset(self):
        self.number = 0

    def get(self):
        return self.number

