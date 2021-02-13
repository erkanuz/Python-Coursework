class Language:

    def __init__(self, main, second):
        self.main = main
        self.second = second

    def print(self):
        print(self.main + " " + self.second, end="")
