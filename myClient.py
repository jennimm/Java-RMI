import Pyro4
# using Python3.4.2

if __name__ == '__main__':
    uri = 'PYRO:TestAPI@localhost:8080'
    remote = Pyro4.Proxy(uri)

    name = input("enter name:")
    response = remote.hello(name)
    print('server said {}'.format(response))
    x = input("Enter number 1:")
    y = input("Enter number 2:")
    z = input("Enter number 3:")
    addition = remote.add(x,y,z)
    print('server return: {}'.format(addition))
    remote.shutdown()
    remote._pyroRelease()
    print('client exiting')