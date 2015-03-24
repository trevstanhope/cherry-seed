import cherrypy
import os
from cherrypy.process.plugins import Monitor

class Test:

    def __init__(self):
        self.hives = ['hive_1', 'hive_2']

    ## Handles all requests to /
    @cherrypy.expose
    def index(self):
        html = open('static/index.html').read()
        return html
    
    ## Handles all requests to /*
    @cherrypy.expose
    def default(self, *args, **kwargs):
        try:
            print "--------------------------------------------"
            print args
            print kwargs
            print "--------------------------------------------"
        except Exception as e:
            print str(e)
        return None

# Main
if __name__ == '__main__':
    serv = Test()
    cherrypy.server.socket_host = "127.0.0.1"
    cherrypy.server.socket_port = 8080
    currdir = os.path.dirname(os.path.abspath(__file__))
    conf = {
        '/': {'tools.staticdir.on':True, 'tools.staticdir.dir' : os.path.join(currdir,'static')},
        '/data': {'tools.staticdir.on':True, 'tools.staticdir.dir' : os.path.join(currdir,'data')},
    }
    cherrypy.quickstart(serv, '/', config=conf)
