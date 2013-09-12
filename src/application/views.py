"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app, login_manager
from decorators import login_required, admin_required
import forms
import models


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


# Setup login and authentication

@login_manager.user_loader
def load_user(userid):
    return models.Student.load(userid)

@login_manager.unauthorized_handler
def unauthorized_user():
    return "Unauthorized."

def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        pass
    return "Login (empty)"

    
# Main application

def list_students():
    """Lists all registered students."""
    students = models.Student.query()
    return render_template('list_students.html', students=students)
    



# Examples: Remove later

def home():
    return redirect(url_for('list_examples'))


def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username

#@login_required
def list_examples():
    """List all examples"""
    examples = models.ExampleModel.query()
    form = forms.ExampleForm()
    if form.validate_on_submit():
        example = models.ExampleModel(
            example_name=form.example_name.data,
            example_description=form.example_description.data,
            added_by=users.get_current_user()
        )
        try:
            example.put()
            example_id = example.key.id()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', examples=examples, form=form)


#@login_required
def edit_example(example_id):
    example = models.ExampleModel.get_by_id(example_id)
    form = forms.ExampleForm(obj=example)
    if request.method == "POST":
        if form.validate_on_submit():
            example.example_name = form.data.get('example_name')
            example.example_description = form.data.get('example_description')
            example.put()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
    return render_template('edit_example.html', example=example, form=form)


#@login_required
def delete_example(example_id):
    """Delete an example object"""
    example = models.ExampleModel.get_by_id(example_id)
    try:
        example.key.delete()
        flash(u'Example %s successfully deleted.' % example_id, 'success')
        return redirect(url_for('list_examples'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_examples'))


#@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


#@cache.cached(timeout=60)
def cached_examples():
    """This view should be cached for 60 sec"""
    examples = models.ExampleModel.query()
    return render_template('list_examples_cached.html', examples=examples)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

