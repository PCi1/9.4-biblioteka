import json


class Books:
    def __init__(self):
        try:
            with open("books.json", "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def all(self):
        return self.books

    def get(self, id):
        return self.books[id]

    def create(self, data):
        data.pop('csrf_token')
        self.books.append(data)

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.books[id] = data
        self.save_all()
    
    def reload_json(self):
        try:
            with open("books.json", 'r') as f:
                self.book = json.load(f)
        except FileNotFoundError:
            self.books = []

    def last_id(self):
        if self.books:
            last_id = self.books[-1].get('id')
        else:
            last_id = 0
        return last_id


books = Books()

class Authors:
    def __init__(self):
        try:
            with open("authors.json", 'r') as f:
                self.authors = json.load(f)
        except FileNotFoundError:
            self.authors = []
    
    def all(self):
        return self.authors

    def create(self, data):
        data.pop('csrf_token')
        self.authors.append(data)
    
    def save_all(self):
        with open("authors.json", "w") as f:
            json.dump(self.authors, f)
    
    def choice_list(self):
        try:
            with open("authors.json", 'r') as f:
                self.authors = json.load(f)
        except FileNotFoundError:
            self.authors = []
        choices_list = []
        for author in authors.all():
            choices_list.append(f"{author.get('first_name')} {author.get('last_name')}")
        return choices_list

authors = Authors()