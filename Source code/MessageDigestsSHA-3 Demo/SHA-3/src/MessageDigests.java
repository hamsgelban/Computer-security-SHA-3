import java.security.MessageDigest;

public class MessageDigests {
	
	//**Generating a message digest with Java**//

	public static void main(String[] args) throws Exception {
		
		// Step 1: Come up with a message we want to hash
		String message = "Hello World";
		byte[] m = message.getBytes();
		
		// Step 2: Create a MessageDigest object
		MessageDigest messageDigest = MessageDigest.getInstance("SHA3-256");
		
		// Step 3: Give the MessageDigest our message
		messageDigest.update(m);
		
		// Step 4: Run the hashing function
		byte[] digest = messageDigest.digest();
		
		System.out.println("String:\t\t\t" + message);
		System.out.println("String length: \t\t" + message.length());
		
		// Step 5: Print the digest in HEX
		System.out.println("digest(Hex): \t\t" + bytesToHex(digest));
		System.out.println("digest(Hex) length:\t" + digest.length);
	}
		
	public static String bytesToHex(byte[] bytes) {
		StringBuilder out = new StringBuilder();
		
		for (byte b : bytes) {
			out.append(String.format("%02X", b));
		}
		
		return out.toString();
	}
}