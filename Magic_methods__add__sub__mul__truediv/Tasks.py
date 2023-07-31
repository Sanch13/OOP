class NewList:
	def __init__(self, lst: list = None):
		self.lst = [] if lst is None else lst

	def __sub__(self, other):


lst1 = NewList([1, 2, 3, 4, 5, 6])
print(id(lst1))
lst2 = NewList([5, 6, 7, 8, 1])
print(id(lst2))