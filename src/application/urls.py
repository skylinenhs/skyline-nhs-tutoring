"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app
from application import views


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)


## Main content

app.add_url_rule('/', 'index', view_func=views.index)
app.add_url_rule('/settings', 'change_user_settings', view_func=views.change_user_settings)

### Student-focused pages
app.add_url_rule('/complete-registration', 'complete_registration', view_func=views.complete_registration)
app.add_url_rule('/student/<student_id>', 'list_individual_student', view_func=views.list_individual_student)

### Admin-focused pages
app.add_url_rule('/students', 'list_all_students', view_func=views.list_all_students, methods=['GET', 'POST'])
app.add_url_rule('/admins', 'list_all_admins', view_func=views.list_all_admins, methods=['GET', 'POST'])
app.add_url_rule('/sessions', 'list_all_sessions', view_func=views.list_all_sessions, methods=['GET', 'POST'])



## Todo: remove examples

# Say hello
app.add_url_rule('/hello/<username>', 'say_hello', view_func=views.say_hello)

# Examples list page
app.add_url_rule('/examples', 'list_examples', view_func=views.list_examples, methods=['GET', 'POST'])

# Examples list page (cached)
app.add_url_rule('/examples/cached', 'cached_examples', view_func=views.cached_examples, methods=['GET'])

# Contrived admin-only view example
app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)

# Edit an example
app.add_url_rule('/examples/<int:example_id>/edit', 'edit_example', view_func=views.edit_example, methods=['GET', 'POST'])

# Delete an example
app.add_url_rule('/examples/<int:example_id>/delete', view_func=views.delete_example, methods=['POST'])


## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

