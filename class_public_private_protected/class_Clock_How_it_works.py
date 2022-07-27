class Clock:
    __MIN_TIME = 0              # private attribute of the class
    __MAX_TIME = 100_000        # private attribute of the class

    def __init__(self, time=0):
        self.__time = 0             # init default
        if self.__check_time(time):  # check input time
            self.__time = time  # assign private (local "__time" object) value time

    @classmethod
    def __check_time(cls, tm):  # check param "tm" (int and diapason)
        return type(tm) is int and cls.__MIN_TIME <= tm < cls.__MAX_TIME

    def set_time(self, tm):  # set param "tm" into private variable self.__time
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):     # return private variable self.__time
        return self.__time


clock = Clock()
print(clock.__dict__)    #0 default from __init__
clock.set_time(15)
print(clock.get_time())    #15
clock.set_time(-1)
print(clock.get_time())    #15
clock.set_time('2')
print(clock.get_time())    #15
clock.set_time(0.1)
print(clock.get_time())  #15
clock.set_time(12345)
print(clock.get_time())  #12345
