# Below is for private
class Emp:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def show(self):
        print(f"name is {self.__name} and id is {self.__id}")


a = Emp("Harry", 101)
print(a._Emp__name)  # __name was private but here accessed and printed directly
a.show()  # this method can also print private members


# below is for protected
class Pro:
    def __init__(self, name, id):
        self._name = name    # "_" is used for protected
        self._id = id        # "_" is used for protected


x = Pro("Alen", 102)
print(x._name)  # _name was protected but here accessed and printed directly
