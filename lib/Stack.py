class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        while True:
            try:
                index = self.items.index(target)
                last_index = self.items.index(self.items[-1])
                if index == 0:
                    return len(self.items) - 1
                else:
                    if index == 1:
                        return last_index - index
                    else:
                        return last_index - index
            except:
                return -1
