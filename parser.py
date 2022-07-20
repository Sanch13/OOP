class Factory:
    def build_sequence(self):  # return empty list
        self.lst = []
        return self.lst

    def build_number(self, string):  # translate str to float
        return float(string)


# Здесь объявляется класс Factory

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()  # copy empty lst[] from factory
        for sub in string.split(","):  # Split ',' list string then Iterate over the elements of the list
            item = factory.build_number(sub)  # from factory translate str to float
            seq.append(item)  # add float item into seq

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
print(res)
# res = [sub for sub in s.split(",")]
# print(res)
# res_2 = list(map(float, res))
# print(res_2)
