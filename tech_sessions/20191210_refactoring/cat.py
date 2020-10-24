
# class Singleton:
#
#     def __new__(cls):
#
#
#     def __init__(self):
#         pass
#
#
# c1 = Cat()
# c2 = Cat()
# c3 = Cat()
#
# print(c1, c2, c3)


class Singletone:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance


s1 = Singletone()
s2 = Singletone()
s3 = Singletone()
print(s1, s2, s3)
