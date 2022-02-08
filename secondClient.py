import Pyro4
# using Python3.4.2

if __name__ == '__main__':
    uri = 'PYRO:TestAPI@localhost:8081'
    remote = Pyro4.Proxy(uri)

    x = input("Enter number 1:")
    y = input("Enter number 2:")
    z = input("Enter number 3:")
    average = remote.average(x,y,z)
    print('server return: {}'.format(average))
    remote.shutdown()
    remote._pyroRelease()
    print('client exiting')