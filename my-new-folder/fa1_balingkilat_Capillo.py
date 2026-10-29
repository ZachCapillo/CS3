class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.number_of_pages}")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Issue: {self.issue_number}")


if __name__ == "__main__":
    print("Library Materials")
    
p1 = Publication("Journey of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
p1.display()
print()

b1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
b1.display()
print()

m1 = Magazine("National Geographic", "Various Authors", 202)
m1.display()
print()
