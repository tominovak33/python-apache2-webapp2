import os
import sys

# Add vendor ('lib') directory to module search path
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)

vendor_dir = os.path.join(current_dir, 'lib')
sys.path.append(vendor_dir)

import webapp2

import routes

# Must be called 'application'
# Otherwise requests will get a "Target WSGI script does not contain WSGI application 'application'" error
# and return a 404 error
# Or alternatively in the relevent Apache Virtual Host file, add the following: define: (where applicationFuncName is the name of the new function)
# WSGICallableObject applicationFuncName
# Where applicationFuncName is the name of the new function rather than `application`
application = webapp2.WSGIApplication(routes.ROUTES, debug=True)
