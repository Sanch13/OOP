class Factory:
    @staticmethod
    def build_sequence():  # return empty list
        return []

    @staticmethod
    def build_number(string):  # translate str to int
        return int(string)


# Здесь объявляется класс Factory

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()  # copy empty lst[] from factory
        for sub in string.split(","):  # Split ',' list string then Iterate over the elements of the list
            item = factory.build_number(sub)  # from factory translate str to int
            seq.append(item)  # add int item into seq

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)

print(res)
# res = [sub for sub in s.split(",")]
# print(res)
# res_2 = list(map(float, res))
# print(res_2)
