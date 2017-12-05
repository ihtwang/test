from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import webapp2


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello World!')


app = webapp.WSGIApplication([('/', MainHandler), ], debug=True)


def main():
    run_wsgi_app(app)


if __name__ == '__main__':
    main()



