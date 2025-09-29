#to define as private:
class Bank:
    def __init__(self, balance):
        self.__balance = balance # balance is now private
    def getBalance(self):
        return self.__balance
    def setBalance(self, balance):
        self.__balance = balance
class Book:
    total_books = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.total_books += 1    
    @classmethod
    def resetTotalBooks(cls):
        """Reset the total book count to zero"""
        cls.total_books = 0
    @classmethod
    def fromDict(cls, data: dict):
        return cls(data["title"], data["author"], data["year"])
    @classmethod
    def __str__(self):
        return 

book1 = Book("python 101", "j. doe", 2023)
data = {"title": "learning python", "author": "john smith", "year": 2020}
book2 = Book.fromDict(data)

class PathUtils:
    @staticmethod
    def getExtension(filename):
        """Return the file extension including the dot"""
        return filename[filename.rfind('.'):] if "." in filename else ""
    @staticmethod
    def getDirectory(filename):
        return filename[:filename.rfind('\\')]
    
    ### TODO
    # static getDirectory - extracts directory path
    # static getBasename - extracts the file or directory name

# usage
print(PathUtils.getExtension("1.txt"))
print(PathUtils.getDirectory("\\workspaces\\pythonFall25\\week04\\class2.py"))