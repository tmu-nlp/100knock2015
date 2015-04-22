import java.util.*;
import java.io.*;
import org.apache.commons.lang.*;


public class nlp04{
    public static void main(String[] args){
        String sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
	String[] words = sent.split(" ");

	HashMap map = new HashMap();
	for(int i=0; i<words.length; i++){
		words[i] = StringUtils.stripEnd(words[i],",");
		words[i] = StringUtils.stripEnd(words[i],".");
		char[] chars = words[i].toCharArray();
		String ex_str;
		if(i==2 || i==6 || i==7 || i==8 || i==9 ||
	           i==10 || i==16 || i==17 || i==20){
			 ex_str = new String(chars,0,2);
			 map.put(i+1,ex_str);
		   }
	 	else{
			 ex_str = new String(chars,0,1);
			 map.put(i+1,ex_str);
		}
        }
	for(int i=1; i<=words.length; i++){
		System.out.println(map.get(i));
	}
    } 
}
