#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
name = ""
class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.out.write("User-Agent:")
        #self.response.out.write(os.environ.get("HTTP_USER_AGENT", "N/A"))
        template = jinja_environment.get_template('header.html')
        self.response.out.write(template.render({}))
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render({}))
        template = jinja_environment.get_template('footer.html')
        self.response.out.write(template.render({}))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('header.html')
        self.response.out.write(template.render({}))
        template = jinja_environment.get_template('workhome.html')
        self.response.out.write(template.render({}))
        template = jinja_environment.get_template('footer.html')
        self.response.out.write(template.render({}))

class Social(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('header.html')
        self.response.out.write(template.render({}))
        template = jinja_environment.get_template('social.html')
        self.response.out.write(template.render({}))
        template = jinja_environment.get_template('footer.html')
        self.response.out.write(template.render({}))
        
class Login(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('login.html')
        self.response.out.write(template.render({}))
        
class Check(webapp2.RequestHandler):
    def get(self):
        global name
        name = self.request.get("uName")
        pword = self.request.get("pWord")
        if (name == "" or pword == ""):
            self.redirect("/admin")
        else:
            self.redirect("/admin-home")
class AdminHome(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'name': name,
            }
        template = jinja_environment.get_template('admin.html')
        self.response.out.write(template.render(template_values))

class Verify(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('googled318d2409bf07f15.html')
        self.response.out.write(template.render({}))        

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/home', MainPage),
                               ('/work', AboutPage),
                               ('/social', Social),
                               ('/admin', Login),
                               ('/in', Check),
                               ('/admin-home', AdminHome),
                               ('/googled318d2409bf07f15.html', Verify)
                               ],
                              debug=True)
