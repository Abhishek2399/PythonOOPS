class Human:
    consciousness = True
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def get_name(self):
        print(f"{id(self)} : {type(self)}")
        return self.name
    
    @classmethod
    def change_consciousness(self):
        self.consciousness = False


if __name__ == "__main__":
    # abhi = Human(name="Abhishek", age=26)
    # rahul = Human(name="Rahul", age=26)
    # print(abhi.consciousness)
    # print(rahul.consciousness)
    # rahul.change_consciousness()
    # print(abhi.consciousness)
    # print(rahul.consciousness)


    h = int(input())
    if h%3 == 0 : print('Fizz')
    if h%5 == 0 : print('Fuzz')
    