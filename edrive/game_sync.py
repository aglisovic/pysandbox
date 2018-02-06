from twisted.web import server, resource
from twisted.internet import reactor
from time import sleep
from random import randint

class MyResource(resource.Resource):
    def render(self, request):
        name = request.args['name'][0]
        sleep(randint(1, 5))
        return "Hello %s!\n" % name

reactor.listenTCP(8080, server.Site(MyResource()))
reactor.run()
