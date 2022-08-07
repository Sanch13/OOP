class Point:
    color = "Red"
    circle = 2


# a = Point()
# b = Point()
#
# print(id(a.color) == id(b.color), a.color, b.color)
# Point.color = 'Grey'
#
# print(id(a.color) == id(b.color), a.color, b.color)
# b.color = 'Green'
#
# print(Point.__dict__)
# print(id(a.color) == id(b.color), a.color, b.color)
#########################################################################################
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


# setattr(Goods, "price", 2048)
# Goods.price = 2048
# setattr(Goods, "inflation", 100)
# Goods.inflation = 100
# print(Goods.__dict__)
#########################################################################################
class Car:
    pass


# setattr(Car, "model", "Тойота")
# setattr(Car, "color", "Розовый")
# setattr(Car, "number", "П111УУ77")
#
# print(Car.__dict__.get('color'))
# print(getattr(Car, "color", False))
#########################################################################################
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


# print(getattr(Notes, "author"))
#########################################################################################
class Dictionary:
    rus = "Питон"
    eng = "Python"


# print(getattr(Dictionary, "rus_word", False))
#########################################################################################
class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "Франция"
tb1.days = 6
TravelBlog.total_blogs += 1
tb2 = TravelBlog()
tb2.name = "Италия"
tb2.days = 5
TravelBlog.total_blogs += 1
#########################################################################################
class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
delattr(fig1, 'color')

# for key in fig1.__dict__:
#     print(key, end=' ')
#########################################################################################
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
# print(True if p1.__dict__.get("job") else False)
# print('job' in p1.__dict__)
#########################################################################################
