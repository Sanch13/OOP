class Node:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_obj

    def set_next(self, obj):
        self.next_obj = obj
