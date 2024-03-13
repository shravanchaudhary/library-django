from main.asgi import *
from library.models import Books, Members

# TODO: Can create data migration to add these data
books = [
    {"id": 1000, "name": "Book 1", "copies": 2},
    {"id": 1001, "name": "Book 2", "copies": 4},
    {"id": 1002, "name": "Book 3", "copies": 1},
    {"id": 1003, "name": "Book 4", "copies": 3},
    {"id": 1004, "name": "Book 5", "copies": 1},
    {"id": 1005, "name": "Book 6", "copies": 2},
    {"id": 1006, "name": "Book 7", "copies": 4},
    {"id": 1007, "name": "Book 8", "copies": 4},
    {"id": 1008, "name": "Book 9", "copies": 3},
    {"id": 1009, "name": "Book 10", "copies": 1},
    {"id": 1010, "name": "Book 11", "copies": 5},
    {"id": 1011, "name": "Book 12", "copies": 5},
    {"id": 1012, "name": "Book 13", "copies": 4},
    {"id": 1013, "name": "Book 14", "copies": 3},
    {"id": 1014, "name": "Book 15", "copies": 3},
    {"id": 1015, "name": "Book 16", "copies": 5},
    {"id": 1016, "name": "Book 17", "copies": 4},
    {"id": 1017, "name": "Book 18", "copies": 1},
    {"id": 1018, "name": "Book 19", "copies": 4},
    {"id": 1019, "name": "Book 20", "copies": 5},
]

members = [
    {"id": 2000, "name": "Member 1"},
    {"id": 2001, "name": "Member 2"},
    {"id": 2002, "name": "Member 3"},
    {"id": 2003, "name": "Member 4"},
    {"id": 2004, "name": "Member 5"},
    {"id": 2005, "name": "Member 6"},
    {"id": 2006, "name": "Member 7"},
    {"id": 2007, "name": "Member 8"},
    {"id": 2008, "name": "Member 9"},
    {"id": 2009, "name": "Member 10"},
    {"id": 2010, "name": "Member 11"},
    {"id": 2011, "name": "Member 12"},
    {"id": 2012, "name": "Member 13"},
    {"id": 2013, "name": "Member 14"},
    {"id": 2014, "name": "Member 15"},
    {"id": 2015, "name": "Member 16"},
    {"id": 2016, "name": "Member 17"},
    {"id": 2017, "name": "Member 18"},
    {"id": 2018, "name": "Member 19"},
    {"id": 2019, "name": "Member 20"},
]

books = Books.objects.bulk_create([Books(**book) for book in books])

members = Members.objects.bulk_create([Members(**member) for member in members])
print(books)
print(members)
