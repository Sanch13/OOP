class Video:
    def create(self, name):
        '''
        создания нового видео с именем name (метод сохраняет имя name в локальном атрибуте name объекта класса Video)
        '''
        self.name = name

    def play(self):
        '''
        воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>")
        '''
        print(f'воспроизведение видео {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        '''
        добавления нового видео (метод помещает объект video класса Video в список)
        '''
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        '''
        проигрывания видео из списка по указанному индексу (индексация с нуля)
        '''
        cls.videos[video_indx].play()



v1 = Video()    # create object #1
v2 = Video()    # create object #2
v1.create("Python")    # create name v1
v2.create("Python ООП")    # create name v2
YouTube.add_video(v1)    # add object v1 into list videos
YouTube.add_video(v2)    # add object v2 into list videos
YouTube.play(0)    # play object from list videos of the index 0
YouTube.play(1)    # play object from list videos of the index 1
