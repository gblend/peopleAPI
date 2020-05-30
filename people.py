
from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "gabrielilochi@gmail.com": {
        "fname": "Gabriel",
        "lname": "Ilochi",
        "email": "gabrielilochi@gmail.com",
        "timestamp": get_timestamp()
    },
    "chinasaoku@gmail.com": {
        "fname": "Rosemary",
        "lname": "Okoro",
        "email": "chinasaoku@gmail.com",
        "timestamp": get_timestamp()
    },
    "jacuriacad@gmail.com": {
        "fname": "Jake",
        "lname": "Obodomechine",
        "email": "jacuriacad@gmail.com",
        "timestamp": get_timestamp()
    },
    "gblend@gmail.com": {
        "fname": "Gabriel",
        "lname": "Ilochi",
        "email": "gblend@gmail.com",
        "timestamp": get_timestamp()
    },
}

# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]



def read_one(email):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people
    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in people?
    if email in PEOPLE:
        person = PEOPLE.get(email)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with email {email} not found".format(email=email)
        )

    return person


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    email = person.get("email", None)

    # Does the person exist already?
    if email not in PEOPLE and email is not None:
        PEOPLE[email] = {
            "lname": lname,
            "fname": fname,
            "email": email,
            "timestamp": get_timestamp(),
        }
        # return make_response(
        #     "{fname} successfully created".format(fname=fname), 201
        # )
        return PEOPLE[email]

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with email {email} already exists".format(email=email)
        )


def update(email, person):
    """
    This function updates an existing person in the people structure
    :param email:   email of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in people?
    if email in PEOPLE:
        PEOPLE[email]["fname"] = person.get("fname")
        PEOPLE[email]["lname"] = person.get("lname")
        PEOPLE[email]["timestamp"] = get_timestamp()

        return PEOPLE[email]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with email {email} not found".format(email=email)
        )


def delete(email):
    """
    This function deletes a person from the people structure
    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if email in PEOPLE:
        del PEOPLE[email]
        return make_response(
            "{email} successfully deleted".format(email=email), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with email {email} not found".format(email=email)
        )