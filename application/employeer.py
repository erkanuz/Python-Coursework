from languages import Language

class Employeer:

    def __init__(self, f_name, l_name, language_main, language_second, age):
        self.f_name = f_name
        self.l_name = l_name
        self.language = Language(language_main, language_second)
        self.age = age

    def full_name(self):
       return f'{self.f_name} {self.l_name}'

    def get_language(self):
        return f'{self.language.main} and {self.language.second}'

    def print(self):
        print(self.full_name()+" ", end="")
        self.get_language()
        print(" "+str(self.age))
