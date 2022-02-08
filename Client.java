package example.hello;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    private Client() {}

    public static void main(String[] args) {

	String host = (args.length < 1) ? null : args[0];
	try {

	    // Get registry
	    Registry registry = LocateRegistry.getRegistry("mira1.dur.ac.uk", 37001);

	    // Lookup the remote object "Hello" from registry
	    // and create a stub for it
	    ServerInterface stub = (ServerInterface) registry.lookup("Hello");

	    // Invoke a remote method
	    String response = stub.sayHello();
	    System.out.println("response: " + response);

	} catch (Exception e) {
		System.err.println("Client exception: " + e.toString());
		e.printStackTrace();
	}
    }
}
