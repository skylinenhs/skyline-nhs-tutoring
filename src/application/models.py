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
    # Visible
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    graduation_year = ndb.IntegerProperty()
    preferences = ndb.StringProperty(choices=SUBJECTS, repeated=True)
    
    # Metadata
    registration_date = ndb.DateTimeProperty(auto_now_add=True)
    is_active = ndb.BooleanProperty(required=True)
    
    def is_authenticated(self):
        return True
        
    def is_active(self):
        return self.is_active
        
    def is_anonymous(self):
        return False
        
    def get_id(self):
        return self.key.name()
        
    @staticmethod
    def load(student_id):
        return models.Student.get_by_key_name(userid)
        
        
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
    
