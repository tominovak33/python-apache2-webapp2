import webapp2

import templates

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_variables = {
            'message': "Hello World"
        }
        templates.render('home', template_variables, self)


class NotFoundHandler(webapp2.RequestHandler):
    def get(self, route):
    	self.error(404)
        template_variables = {
            'message': "404 - Page Not Found"
        }
        templates.render('404', template_variables, self)
