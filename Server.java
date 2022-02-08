package example.hello;
	
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
	
public class Server implements ServerInterface {

    public Server() { }

    public String sayHello() {
	return "Sucessful remote invocation!";
    }
	
    public static void main(String args[]) {
	
	try {
	    // Create server object
	    Server obj = new Server();

	    // Create remote object stub from server object
	    ServerInterface stub = (ServerInterface) UnicastRemoteObject.exportObject(obj, 0);

	    // Get registry
	    Registry registry = LocateRegistry.getRegistry("mira1.dur.ac.uk", 37001);

	    // Bind the remote object's stub in the registry
	    registry.bind("Hello", stub);

	    // Write ready message to console
	    System.err.println("Server ready");
	} catch (Exception e) {
	    System.err.println("Server exception: " + e.toString());
	    e.printStackTrace();
	}
    }
}
