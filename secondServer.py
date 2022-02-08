import Pyro4
# using Python3.4.2

@Pyro4.expose
class TestAPI:
    velocity="yes"
    def __init__(self, daemon):
        self.daemon = daemon
    def hello(self, msg):
        print('client said {}'.format(msg))
        return 'hello {0} \n'.format(msg)
    def average(self, x, y, z):
        print("client's numbers are: {0}, {1}, {2}".format(x,y,z))
        summ = int(x) + int(y) + int(z)
        return summ/3
    @Pyro4.oneway   # in case call returns much later than daemon.shutdown
    def shutdown(self):
        print('shutting down...')
        self.daemon.shutdown()

if __name__ == '__main__':
    daemon = Pyro4.Daemon(port=8081)
    tapi = TestAPI(daemon)
    uri = daemon.register(tapi, objectId='TestAPI')
    daemon.requestLoop()
    print('exited requestLoop')
    daemon.close()
    print('daemon closed')
