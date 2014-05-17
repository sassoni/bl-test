"""A simple webapp2 server."""

import webapp2
import validdate

form="""
<form method="post">
    Birthday:
    <br>
    <label> Month
    <input type="text" name="month">
    </label>
    <label> Day
    <input type="text" name="day">
    </label>
    <label> Year
    <input type="text" name="year">
    </label>
    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
    def post(self):
        birthday_month = validdate.valid_month(self.request.get('month'))
        birthday_day = validdate.valid_day(self.request.get('day'))
        birthday_year = validdate.valid_year(self.request.get('year'))
        
        if (birthday_month and birthday_day and birthday_year):
           self.response.out.write("This is a valid date!")
        else:
            self.response.out.write("Sorry, the date is not valid!")
            
application = webapp2.WSGIApplication([('/', MainPage)], debug=True)