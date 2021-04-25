class PQ:

    def __init__(self):
        self.values = []
    
    def insert(self, value):
        self.values.append(value)
        self.__swim_up(len(self.values) - 1)

    def delMin(self):

        if len(self.values) == 0: 
            return None

        # swap the first and last element of the values
        self.swap(0, len(self.values) - 1)
        output = self.values.pop()
        self.__sink(0)
        return output

    def size(self):
        return len(self.values)
    
    def contains(self, targetValue):
        for value in self.values:
            if value == targetValue:
                return True
        return False

    def isEmpty(self):
        return self.size() == 0


    def __sink(self, targetIndex):
        
        queueSize = len(self.values)


        while True:
            leftIndex = 2 * targetIndex + 1
            rightIndex = 2 * targetIndex + 2

            smaller = leftIndex

            if rightIndex < queueSize and self.values[rightIndex] < self.values[smaller]:
                smaller = rightIndex
            
            # needs to be >= here because the case of just two values
            if leftIndex >= queueSize or self.values[smaller] > self.values[targetIndex]:
                break

            self.swap(smaller, targetIndex)
            targetIndex = smaller

    def decreaseKey(self, targetValue, priority):
            index = 0
            for value in self.values:
                if value == targetValue:
                    value.priority = priority
                    self.__swim_up(index)
                    # self.__sink(index)
                index += 1


    def __swim_up(self, targetIndex):
        parent_index = (targetIndex - 1) // 2

        while self.values[targetIndex] < self.values[parent_index] and targetIndex > 0:

            self.swap(parent_index, targetIndex)

            targetIndex = parent_index
            parent_index = (targetIndex - 1) // 2


    def swap(self, firstIndex, secondIndex):
        tmp = self.values[firstIndex]
        self.values[firstIndex] = self.values[secondIndex]
        self.values[secondIndex] = tmp


class NoDupePQ(PQ):

    def __init__(self):

        super().__init__()
        self.pointers = {}

    def insert(self, value):
        
        if self.contains(value.name):
            return False

        self.pointers[value.name] = len(self.values) + 1
        super().insert(value)
        return True

    def delMin(self):
        output = super().delMin()

        if output is not None:
            self.pointers.pop(output.name)

        return output


    def contains(self, targetValue):
        return self.pointers.get(targetValue) is not None

    def swap(self, firstIndex, secondIndex):
        firstItemName = self.values[firstIndex].name
        secondItemName = self.values[secondIndex].name

        self.pointers[firstItemName], self.pointers[secondItemName] = self.pointers[secondItemName], self.pointers[firstItemName]

        super().swap(firstIndex, secondIndex)



class PQItem:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __eq__(self, name):
        return self.name == name
    
    def __ge__(self, other):
        return self.priority >= other.priority

    def __gt__(self, other):
        return self.priority > other.priority
    
    def __le__(self, other):
        return self.priority <= other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return "name is: {0} and priority is: {1}".format(self.name, self.priority)




test = NoDupePQ()

test.insert(PQItem("eric", 15))
test.insert(PQItem("nani", 21))
test.insert(PQItem("koro", 9))
test.insert(PQItem("tada", 27))

test.decreaseKey("nani", 12)

print(test.contains("koro"))
print(test.delMin())


print(test.contains("koro"))

print(test.delMin())
print(test.contains("nani"))

print(test.delMin())