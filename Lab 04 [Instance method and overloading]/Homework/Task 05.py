 

#Task 5
class Author:
    def __init__(self, name = None):
        self.name=name
        self.books= {}
        self.c = 0
        if name == None:
            print("A book can not be added without author name")

    def addBook(self, title, genre):
        if self.name != None:
            if genre not in self.books:
                self.books[genre] = [title]
            else:
                self.books[genre] += [title]
            self.c += 1

    def setName(self, name):
        self.name = name

    def printDetail(self):
        print(f"Number of Book(s): {self.c}\nAuthor Name: {self.name}")
        for i in self.books:
            s = i +": "
            k = self.books[i]
            for j in k:
                s += j +", "
            print(s[:-2])

a1 = Author()
print("=================================")
a1.addBook("Ice", "Science Fiction")
print("=================================")
a1.setName("Anna Kavan")
a1.addBook("Ice", "Science Fiction")
a1.printDetail()
print("=================================")
a2 = Author("Humayun Ahmed")
a2.addBook("Onnobhubon", "Science Fiction")
a2.addBook("Megher Upor Bari", "Horror")
print("=================================")
a2.printDetail()
a2.addBook("Ireena", "Science Fiction")
print("=================================")
a2.printDetail()
print("=================================")