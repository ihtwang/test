import webapp2
from google.appengine.ext import db
from google.appengine.api import memcache, users


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('Hello %s' % user.nickname())
        else:
            self .response.out.write('Hello World! [<a href=%s>sign in</a>]' % (
                users.create_login_url(self.request.uri)
            ))

        self.response.out.write('<h1>The Greatest Blog</h1>')

        if user:
            self.response.out.write('''
                <form action="/post" method=post>
                Title:
                <br><input type=text name=title>
                <br>Body:
                <br><textarea name=body rows=3 cols=60></textarea>
                <br><input type=submit value="post">
                </form>
                <hr>
             ''')

        posts = memcache.get('Key')  # check cache first
        if not posts:
            posts = BlogPost.all().order('-timestamp').fetch(10)
            memcache.add('Key', posts)  # cache this object

        # posts = BlogPost.all().order('-timestamp').fetch(10)
        for post in posts:
            self.response.out.write('''<hr>
            <strong>%s</strong><br>%s
            <blockquote>%s</blockquote>
            ''' % (
                post.title, post.timestamp, post.body
            ))


class BlogPost(db.Model):
    title = db.StringProperty()
    body = db.TextProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)


class BlogEntry(webapp2.RequestHandler):
    def post(self):
        post = BlogPost()
        post.title = self.request.get('title')
        post.body = self.request.get('body')
        post.put()
        memcache.delete('Key')
        self.redirect('/')

        #self.response.out.write('<b>%s</b><br><hr>%s' % (
        #    self.request.get('title'),
        #    self.request.get('body')
        #))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/post', BlogEntry),
], debug=True)


