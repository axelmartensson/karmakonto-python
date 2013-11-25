# -*- test-case-name: test.group -*-
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

from calendar import calendar

class Individual(Resource):
    def __init__(self,db, year, group):
        Resource.__init__(self)
        self.db = db
        self.year = year
        self.group = group

    def render_GET(self, request):
        return "<html><body><pre>Karma-item: %s \n\
        karma-group:%s</pre></body></html>" % (self.year, self.group)

class Group(Resource):
    def __init__(self,db, name):
        Resource.__init__(self)
        self.db = db
        self.name = name
    def getChild(self, childname, request):
        return Individual(self.db,childname, self.name)

    def render_GET(self, request):
        return "<html><body><pre>karma-group: %s</pre></body></html>" % self.name 

class AllGroups(Resource):
    def __init__(self,db):
        Resource.__init__(self)
        self.db = db

    def getChild(self, childname, request):
        if childname == "": #le hack for getting the root resource
            return self;
        return Group(self.db, childname);

    def render_GET(self, request):
        return "<html><body><pre>list of all karma-groups</pre></body></html>"  
if __name__ == "__main__":
    root = AllGroups(None)
    factory = Site(root)
    reactor.listenTCP(8080, factory)
    reactor.run()
