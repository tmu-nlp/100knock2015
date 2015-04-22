import java.util.*;
import java.io.*;
import org.apache.commons.lang.*;


public class nlp05{
    public static void main(String[] args){
        String sent ="I am an NLPer";
	double N = Double.parseDouble(args[0]);
	String type = args[1];


	if(args.length==0)
		System.out.println("Please input a intNumber(1~5)");
	else if(N!=(int)N || (N>5 && N<1))
		System.out.println("An error number was inputed");
	else{
		if(type.equals("word")){
			int n = (int)N;
			String[] words = sent.split(" ");
			for(int i=0; i<words.length; i++){
				words[i] = StringUtils.stripEnd(words[i],",");
				words[i] = StringUtils.stripEnd(words[i],".");
			}
			String[] toks = new String[words.length+n-1];

			for(int i=0; i<words.length+n-1; i++){
				if(i<n-1)	toks[i] = "<s>";
				else toks[i] = words[i-n+1];
			}
			
			for(int i=0; i<toks.length-n+1; i++){
				String gram = "";
				for(int j=0; j<N; j++){
					gram = gram+" "+toks[i+j];
				}
				System.out.println(gram);
			}
		}
		else if(type.equals("char")){
			int n = (int)N;
			char[] chars = sent.toCharArray();
			String[] toks = new String[sent.length()+n-1];
			
			for(int i=0; i<chars.length+n-1; i++){
				if(i<n-1)	toks[i] = "<s>";
				else toks[i] = chars[i-n+1]+"";
			}
			for(int i=0; i<toks.length-n+1; i++){
				String gram = "";
				for(int j=0; j<N; j++){
					gram = gram+" "+toks[i+j];
				}
				System.out.println(gram);
			}
		}
	}

    } 
}
