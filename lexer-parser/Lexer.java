
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import java.util.Stack;
import java.util.Arrays;

class Token {
	public char cmd;
	public int  numTimes;

	public Token(char cmd, int numTimes) {
		this.cmd = cmd;
		this.numTimes = numTimes;
	} 
}


public class Lexer {
	private static Stack<Token> tokenStack = new Stack<Token>();
	private static char[] acceptedChars = {'+', '-', '<', '>', '.', ',', '[', ']'};
	
	private static void printTokenStack() {
		
		while(tokenStack.empty() == false) {
			Token token = tokenStack.pop();

			System.out.println("CMD: " + token.cmd);
			System.out.println("VALUE: " + token.numTimes + "\n");
		}
	}

	private static boolean contains(char[] array, char key) {
		for (char value : array) {
			if (value == key) {
				return true;
			}
		}

		return false;
	}

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
      		
      		while (fis.available() > 0) {
        		char cur = (char) fis.read();

        		if(!contains(acceptedChars, cur)) { continue; }

        		int numTimes = 1;

        		char next;
        		while ((next = (char) fis.read()) == cur) {
        			numTimes += 1;
        		}
        		
				Token token = new Token(cur, numTimes);
				tokenStack.push(token);
      		}

      		printTokenStack();

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