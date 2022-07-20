TYPE_OS = 2  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:  # здесь объявляйте класс Dialog
    def __new__(cls, *args, **kwargs):
        __link = None
        if TYPE_OS == 1:
            __link = super().__new__(DialogWindows)

        else:
            __link = super().__new__(DialogLinux)

        __link.name = args[0]
        return __link


dg = Dialog('1212')
print(dg.name_class)