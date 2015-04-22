/**
 * 
 */
package java_new100knock;

import java.util.*;

/**
 * @author kitagawayoshiaki
 *
 */

public class Knock3 {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
        String sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
        String[] sentence_list = sentence.split(" ", 0);
        List <Integer>token_size_list = new ArrayList<Integer>();
        
        for(int i = 0; i < sentence_list.length; ++i ){
        	if (sentence_list[i].endsWith(",")){
        	token_size_list.add(sentence_list[i].length()-1);
        	}
        	else if (sentence_list[i].endsWith(".")){
            	token_size_list.add(sentence_list[i].length()-1);
            	}
        	else
        	token_size_list.add(sentence_list[i].length());
        }
        for(int i = 0; i < token_size_list.size(); ++i ){
        	System.out.println(token_size_list.get(i));
        }
        
	}
}
