class AppStore:
    def __init__(self):
        self.store = {}

    def add_application(self, app):
        self.store[id(app)] = app

    def remove_application(self, app):
        self.store.pop(id(app))

    def block_application(self, app):
        obj = self.store.get(id(app), False)
        if not obj:
            return False
        obj.blocked = True
        print(obj)
        return True

    def total_apps(self):
        return len(self.store)


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


