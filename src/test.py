import jsonrpclib
from simplejson import loads
server = jsonrpclib.Server("http://localhost:8080")

result = loads(server.parse("Hello world.  It is so beautiful"))
print "Result", result['coref']