from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode , Decimal
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import decimal
from wsgiref.simple_server import make_server

class TempTrajetService(ServiceBase):
    
    @rpc( Decimal,Decimal,Integer, Integer,  _returns=Decimal)
    def duration_time(ctx, speed, distance, nbstops, timeStop):
        ctx.transport.resp_headers['Access-Control-Allow-Origin'] = '*'

        return (distance/speed)+(timeStop*nbstops)


application = Application([TempTrajetService], 'spyne.examples.hello.soap', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
wsgi_application = WsgiApplication(application)

app=wsgi_application
##server = make_server('127.0.0.1', 8000, wsgi_application)
##server.serve_forever()