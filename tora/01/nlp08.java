import java.util.*;
import java.io.*;
import java.lang.*;
import org.apache.commons.lang.*;


public class nlp08{
    public static void main(String[] args){
		String str = "I am an NLPer";
		System.out.println(encode(str));
		System.out.println(decode(encode(str)));
    } 

	public static String encode(String str){
		char[] chars = str.toCharArray();
		for(int i=0; i<chars.length; i++){
			char currChar = chars[i]; 
			if(Character.isLowerCase(currChar))
				chars[i] = (char)(219-currChar);
			else
				continue;
		}
		String result = new String(chars);
		return result;
	}

	public static String decode(String str){
		char[] chars = str.toCharArray();
		for(int i=0; i<chars.length; i++){
			char currChar = chars[i]; 
			if(Character.isLowerCase(currChar))
				chars[i] = (char)(219-currChar);
			else
				continue;
		}
		String result = new String(chars);
		return result;
	}

}
