import java.util.*;
import java.io.*;
import org.apache.commons.lang.*;


public class nlp03{
    public static void main(String[] args){
        String sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
	String[] words = sent.split(" ");
	for(int i=0; i<words.length; i++){
		words[i] = StringUtils.stripEnd(words[i],",");
		words[i] = StringUtils.stripEnd(words[i],".");
		System.out.print(words[i].length());
        }
    } 
}
