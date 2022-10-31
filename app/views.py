from flask import render_template
from flask_appbuilder import ModelView
from flask_appbuilder import BaseView, expose
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from app import appbuilder

"""
    Define you Views here
"""
 
class HelloWorld(BaseView):
    """ This first view of the tutorial """
    route_base = "/hello"  
 
    @expose("/")
    def hello(self):
        return "Hello, World! from Software Testing Help"

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

# at the end of the file
appbuilder.add_view_no_menu(HelloWorld())
