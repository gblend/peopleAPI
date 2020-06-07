
from flask import abort, make_response, jsonify
from datetime import datetime
from config import db
from models import Person, PersonSchema

#init schema
person_schema = PersonSchema()
people_schema = PersonSchema(many=True)


# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return: sorted list of people
    """

    # Create the list of people from our data
    people = Person.query.order_by(Person.fname).all()

    # Serialize the data for the response
    return people_schema.jsonify(people)


def read_one(email):
    # Get the person requested
    person = Person.query.filter(Person.email == email).one_or_none()

    # Did we find a person?
    if person is not None:

        # Serialize the data for the response
        return person_schema.jsonify(person)

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404, "Person with email {email} not found".format(email=email)
        )


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname")
    fname = person.get("fname")
    email = person.get("email")
    
    create_person = Person(fname, lname, email)
        
    existing_person = Person.query.filter(Person.email == email).one_or_none()

    # Can we insert this person?
    if existing_person is None:

        # Add the person to the database
        db.session.add(create_person)
        db.session.commit()

        # Serialize and return the newly created person in the response
        return person_schema.jsonify(create_person), 201

    # Otherwise, nope, person exists already
    else:
        abort(
            406, "Person with email {email} already exists".format(email=email)
        )


def update(email, person):
    """
    This function updates an existing person in the people structure
    :param email:   email of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    
        # Get the person requested from the db into session
    update_person = Person.query.filter(Person.email == email).one_or_none()

    # Try to find an existing person with the same name as the update
    fname = person.get("fname")
    lname = person.get("lname")
    email = person.get("email")

    # Are we trying to find a person that does not exist?
    if update_person is None:
        abort(
            404, "Person with email {email} not found".format(email=email)
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in person into a db object
        update_person.fname = fname
        update_person.lname = lname
        update_person.email = email

        # merge the new object into the old and commit it to the db
        db.session.commit()

        # return updated person in the response
        data = person_schema.jsonify(person)

        return data, 200
        


def delete(email):
    """
    This function deletes a person from the people structure
    :param email:   email address of person to delete
    :return:        200 on successful delete, 404 if not found
    """
        # Get the person requested
    person = Person.query.filter(Person.email == email).one_or_none()

    # Did we find a person?
    if person is not None:
        db.session.delete(person)
        db.session.commit()
        
        return make_response(
            "Record with email {email} deleted successfully".format(email=email), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with email {email} not found".format(email=email)
        )

