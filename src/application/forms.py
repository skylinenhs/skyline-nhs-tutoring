"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators
from wtforms.ext.appengine.ndb import model_form

import models

class MultiCheckboxField(wtf.SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = wtf.widgets.ListWidget(prefix_label=False)
    option_widget = wtf.widgets.CheckboxInput()


class ClassicExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])

# App Engine ndb model form example
ExampleForm = model_form(models.ExampleModel, wtf.Form, field_args={
    'example_name': dict(validators=[validators.Required()]),
    'example_description': dict(validators=[validators.Required()]),
})

class NewStudentForm(wtf.Form):
    name = wtf.TextField('Name', validators=[validators.Optional()])
    email = wtf.TextField('Email', validators=[validators.Required(), validators.Email()])
    graduation_year = wtf.TextField('Graduation year', validators=[validators.Optional()])
    preferences = MultiCheckboxField('Preferences', choices=zip(models.SUBJECTS, models.SUBJECTS), validators=[validators.Optional()])
