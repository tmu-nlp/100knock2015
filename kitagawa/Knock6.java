/**
 * 
 */
package java_new100knock;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @author kitagawayoshiaki
 *
 */
public class Knock6 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String word1 = "paraparaparadise";
		String word2 = "paragraph";
		List <String>char_bigram_list1= new ArrayList<String>();
		List <String>char_bigram_list2= new ArrayList<String>();
		Set<String> setsum = new HashSet<String>();
		Set<String> setmul = new HashSet<String>();
		
		//文字ngramの獲得と和集合の獲得
		for (int i=0; i<(word1.length()-1); i++){
			char_bigram_list1.add(word1.substring(i,i+2));
			setsum.add(word1.substring(i,i+2));
		}
		for (int i=0; i<(word2.length()-1); i++){
			char_bigram_list2.add(word1.substring(i,i+2));
			setsum.add(word1.substring(i,i+2));
		}
       
		//積集合
		for (int i=0; i<char_bigram_list2.size(); i++){
			if (setsum.contains(char_bigram_list2.get(i))){
				setmul.add(char_bigram_list2.get(i));
			}
		}
		//差集合
		Set<String> setdif = new HashSet<String>(setsum);
        setdif.removeAll(setmul);
		
          
		System.out.println("和集合");	
	    System.out.println(setsum.toString());
	    System.out.println("差集合");	
	    System.out.println(setdif.toString());
	    System.out.println("積集合");	
	    System.out.println(setmul.toString());	
	}
}

