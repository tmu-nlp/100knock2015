import java.util.*;
import java.io.*;
import org.apache.commons.lang.*;


public class bigramChar{
    public static void main(String[] args){
		//make_bigram("abc");
	}

    public static String[] parsetoBigram(String input_str){
	int n = 2;
	String[] bi_grams = new String[input_str.length()];

	char[] chars = input_str.toCharArray();
	String[] toks = new String[input_str.length()+n-1];
	
	for(int i=0; i<chars.length+n-1; i++){
		if(i<n-1)	toks[i] = "<s>";
		else toks[i] = chars[i-n+1]+"";
	}
	for(int i=0; i<toks.length-n+1; i++){
		String gram = "";
		for(int j=0; j<n; j++){
			gram = gram+" "+toks[i+j];
		}
		bi_grams[i] = gram;
	}

	return bi_grams;
    } 
}
