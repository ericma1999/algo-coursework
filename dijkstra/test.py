test = [1,2,3,4]

def __permutations(size, values, output):
    if size == 1:
        output.append(values.copy())
    else:

        __permutations(size - 1, values, output)

        for i in range(size - 1):
            if size % 2 == 0:
                values[i], values[size - 1] = values[size - 1], values[i]
            else:
                values[0], values[size - 1] = values[size - 1], values[0]
            
            __permutations(size - 1, values, output)

output = []
__permutations(len(test), test, output)

print(output)