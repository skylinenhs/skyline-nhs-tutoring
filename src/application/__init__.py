"""
Initialize Flask app

"""
import os.path

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension
from gae_mini_profiler import profiler, templatetags
from werkzeug.debug import DebuggedApplication
from flaskext import login #, openid

app = Flask('application')
app.config.from_object('application.settings')

# Custom login manager
login_manager = login.LoginManager()
login_manager.init_app(app)
#oid = openid.OpenID(app, os.path.join(basedir, 'tmp'))

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


@app.context_processor
def inject_profiler():
    return dict(profiler_includes=templatetags.profiler_includes())

# Pull in URL dispatch routes
import urls

# Flask-DebugToolbar (only enabled when DEBUG=True)
toolbar = DebugToolbarExtension(app)

# Werkzeug Debugger (only enabled when DEBUG=True)
if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

# GAE Mini Profiler (only enabled on dev server)
app.wsgi_app = profiler.ProfilerWSGIMiddleware(app.wsgi_app)


