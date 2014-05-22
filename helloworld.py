"""A simple webapp2 server."""
import os 

import jinja2
import webapp2
import sutil as s

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class MainPage(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
        
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    #def print_form(self, error="", month="", day="", year=""):
        #self.response.out.write(form % {"error": error, "month": s.escape_html(month), "day": s.escape_html(day), "year": s.escape_html(year)})
 
    def get(self):
        self.render("birthday_form.html")
        #self.print_form()
    
    def post(self):
        birthday_month = self.request.get('month')
        birthday_day = self.request.get('day')
        birthday_year = self.request.get('year')
        
        if (s.valid_month(birthday_month) and s.valid_day(birthday_day) and s.valid_year(birthday_year)):
           self.redirect("/thanks")
        else:
           self.print_form("Sorry, the date is not valid!", birthday_month, birthday_day, birthday_year)
           
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("This is a valid date!")
            
application = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)], debug=True)