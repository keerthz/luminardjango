class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        return book(self.pages+other.pages)

    def __sub__(self, other):
        return (self.pages - other.pages)

    def __str__(self):
        return str(self.pages)

ob=book(100)
ob2=book(200)
ob3=book(300)
print(ob+ob2+ob3)
