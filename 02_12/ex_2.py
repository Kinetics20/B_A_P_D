import math


class SequenceOfNumbers:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        return math.ceil((self.stop - self.start) / self.step)

    def __getitem__(self, index):  # obj[index]
        if index >= len(self):
            raise IndexError('Index too big')
        if index < 0:
            raise IndexError('No negative indexes please!')
        return self.start + index * self.step


def middle_elements(list_of_lists):
    output = []
    for inner_list in list_of_lists:
        length = len(inner_list)
        if length == 0:
            continue
        middle_index = length // 2
        output.append(inner_list[middle_index])
    return output


print(middle_elements([
    [6, 7, 8, 9, 10],
    ["Kto", "to", "taki?"],
    [],
    ["sześć", "siedem", "osiem", "dziewięć"]
]))
