"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb

CATEGORIES = ["stem", "humanities"]
SUBJECTS = [
    "physics",
    "biology",
    "chemistry",
    "math",
    "science/math (other)",
    "english",
    "spanish",
    "french",
    "chinese",
    "humanities (other)"
]

class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    graduation_year = ndb.IntegerProperty(required=True)
    preferences = ndb.StringProperty(repeated=True, choices=SUBJECTS)
    registration_date = ndb.DateTimeProperty(auto_now_add=True)
    
class Tutor(ndb.Model):
    student = ndb.KeyProperty(required=True, kind=Student)
    signup_date = ndb.DateTimeProperty(required=True, auto_now_add=True)
    present = ndb.BooleanProperty(required=True)
    verified_by = ndb.UserProperty()
    
class TutoringSession(ndb.Model):
    date = ndb.DateProperty(required=True)
    time = ndb.TimeProperty(required=True)
    
    spots_open = ndb.IntegerProperty(required=True)
    category = ndb.StringProperty(required=True, choices=CATEGORIES)
    location = ndb.StringProperty(required=True)
    
    extra_information = ndb.TextProperty()
    
    signup_list = ndb.KeyProperty(kind=Tutor, repeated=True)
    waiting_list = ndb.KeyProperty(kind=Tutor, repeated=True)
    
