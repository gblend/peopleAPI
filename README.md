#PeopleAPI
Developed using Pyhthon 3, Flask, Connexion, Marsmallow, SQLAlchemy, Mysql, SQLite, Html, Javascript, CSS and swagger-ui

The peopleAPI includes the following endpoints:
1. /api/people 
   This function responds to a request for /api/people
   with the complete lists of people

2. /api/people/{email} 
    This function responds to a request for /api/people
    with the complete lists of people

3. /api/people/{person} 
    This function creates a new person in the people structure
    based on the passed in person data

4. /api/people/{email, people}
    This function updates an existing person in the people structure

5. /api/people/{email}
    This function deletes a person from the people structure
    :param email:   email address of person to delete