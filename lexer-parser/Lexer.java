

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

class Token {
	public char cmd;
	public int  numTimes;

	public Token(char cmd, int numTimes) {
		this.cmd = cmd;
		this.numTimes = numTimes;
	} 
}


public class Lexer {
	private static int readFile(String filename) {
		File file = new File(filename);
   
   		if (!file.exists()) {
      		System.out.println(filename + " does not exist.");
      		return 1;
   		}
    
    	if (!(file.isFile() && file.canRead())) {
      		System.out.println(file.getName() + " cannot be read from.");
      		return 1;
    	}

    	try {
    		FileInputStream fis = new FileInputStream(file);
      		char current;
      
      		while (fis.available() > 0) {
        		current = (char) fis.read();
        		System.out.print(current);
      		}
    	} catch (IOException e) {
      		e.printStackTrace();
    		return 1;
    	}

    	return 0;
	}


	public static void main(String[] args) {
		if (readFile(args[0]) == 1) {
			System.out.println("Dammit there is an error");
		}
	}
}