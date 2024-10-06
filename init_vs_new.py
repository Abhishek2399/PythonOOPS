class School:
    """
    Following class is a representation of a School entity which will be only one ( for the singleton demonstration )
    """
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name:str=""):
        self.name = name


class Student:
    """
    Following class is used to represent Student entity which can be multiple
    """
    def __new__(cls, *args, **kwargs)->object:
        """
        Following dunder method is used to instantiate a new object for the current class, which is cls

        Returns:
            object: Object of the current class which is Student
        """
        print(f"New Student created")
        instance = super().__new__(cls)
        return instance
    

    def __init__(self, name="", age="")->None:
        """
        Following dunder method is used to initialize the attributes of the newly created instance

        Args:
            name (str, optional): Name of the student. Defaults to "".
            age (str, optional): Age of the student. Defaults to "".
        """
        print(f"Initialized Student")
        self.name = name
        self.age = age

    

if __name__ == "__main__":
    # creating two instance of school and checking if they are same
    school1 = School()
    school2 = School()
    print(f"School1 == School2 : {school1 == school2}")

    stud1 = Student()
    stud2 = Student()
    print(f"Student1 == Student2 : {stud1 == stud2}")