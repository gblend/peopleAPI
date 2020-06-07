import os
from config import db
from models import Person

# Data to initialize database with
PEOPLE = [
    {
        "fname": "Gabriel",
        "lname": "Ilochi",
        "email": "gabrielilochi@gmail.com"
    },
    {
        "fname": "Rosemary",
        "lname": "Okoro",
        "email": "chinasaoku@gmail.com"
    },
    {
        "fname": "Jake",
        "lname": "Obodomechine",
        "email": "jacuriacad@gmail.com"
    },
    {
        "fname": "Gabriel",
        "lname": "Ilochi",
        "email": "gblend@gmail.com"
    },
]

# Delete database file if it exists currently
# if os.path.exists('people.db'):
#     os.remove('people.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get('lname'), fname=person.get('fname'), email=person.get('email'))
    db.session.add(p)

db.session.commit()