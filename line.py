class Line:
    def __init__(self):
        self.array = []

    def line_add(self, el):
        self.array.append(el)

    def line_ex(self):
        if self.array:
            return self.array.pop(0)
        else:
            return None

    def __add__(self, other):
        new_array = self.array + other.array
        new_line = Line()
        for el in new_array:
            new_line.line_add(el)
        return new_line

    def __iadd__(self, other):
        for el in other.array:
            self.line_add(el)
        return self

    def __len__(self):
        return len(self.array)

    def __str__(self):
        st = ""
        if self.array:
            st += "-" * len(self) * 2
            st += "\n"
            for el in self.array:
                st += "<"
                st += str(el)
            st += "\n"
            st += "-" * len(self) * 2
        else:
            st += "_"
        return st
