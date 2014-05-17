"""A simple webapp2 server."""

import webapp2
import sutil as s

form="""
<form method="post">
    Birthday:
    <br>
    <label> Month <input type="text" name="month" value="%(month)s"> </label>
    <label> Day <input type="text" name="day" value="%(day)s"> </label>
    <label> Year <input type="text" name="year" value="%(year)s"> </label>
    <div style="color:red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def print_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error, "month": s.escape_html(month), "day": s.escape_html(day), "year": s.escape_html(year)})
 
    def get(self):
        self.print_form()
    
    def post(self):
        birthday_month = self.request.get('month')
        birthday_day = self.request.get('day')
        birthday_year = self.request.get('year')
        
        if (s.valid_month(birthday_month) and s.valid_day(birthday_day) and s.valid_year(birthday_year)):
           self.response.out.write("This is a valid date!")
        else:
           self.print_form("Sorry, the date is not valid!", birthday_month, birthday_day, birthday_year)
            
application = webapp2.WSGIApplication([('/', MainPage)], debug=True)