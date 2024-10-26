import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class FileChecksum {

	//**Java SHA3-256 File Checksum**//

	private static byte[] checksum(String filePath, String algorithm) {

		MessageDigest md;
		try {
			md = MessageDigest.getInstance(algorithm);
		} catch (NoSuchAlgorithmException e) {
			throw new IllegalArgumentException(e);
		}

		try (InputStream is = new FileInputStream(filePath);
				DigestInputStream dis = new DigestInputStream(is, md)) {
			while (dis.read() != -1) ; //empty loop to clear the data
			md = dis.getMessageDigest();
		} catch (IOException e) {
			throw new IllegalArgumentException(e);
		}
		return md.digest();

	}

	public static String bytesToHex(byte[] bytes) {
		StringBuilder sb = new StringBuilder();
		for (byte b : bytes) {
			sb.append(String.format("%02x", b));
		}
		return sb.toString();
	}

	public static void main(String[] args) throws IOException {

		String algorithm = "SHA3-256";

		// get file path from resources
		String filePath = "C:\\Users\\nalem\\OneDrive\\Desktop\\CMPS385 Java\\SHA-3\\src\\sha-file.txt";

		byte[] hashInBytes = checksum(filePath, algorithm);
		System.out.println("Hash before any changes in the text file:\n" + bytesToHex(hashInBytes));


		// Write in the same text file
		try {
			FileWriter myWriter = new FileWriter("C:\\Users\\nalem\\OneDrive\\Desktop\\CMPS385 Java\\SHA-3\\src\\sha-file.txt");
			myWriter.write("Hello World !!");
			myWriter.close();
			System.out.println("\nSuccessfully wrote to the file.\n");
		} catch (IOException e) {
			System.out.println("\nAn error occurred.\n");
			e.printStackTrace();
		}

		// get file path from resources
		String filePath2 = "C:\\Users\\nalem\\OneDrive\\Desktop\\CMPS385 Java\\SHA-3\\src\\sha-file.txt";

		byte[] hashInBytes2 = checksum(filePath2, algorithm);
		System.out.println("Hash After modified the text file:\n" + bytesToHex(hashInBytes2));
	}

}