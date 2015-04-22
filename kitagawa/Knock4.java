/**
 * 
 */
package java_new100knock;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * @author kitagawayoshiaki
 *
 */
public class Knock4 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
		String[] sentence_list = sentence.split(" ", 0);
		List <String>symbols= new ArrayList<String>();
		HashMap<String,Integer> map = new HashMap<String,Integer>();
		for (int i = 0; i<sentence_list.length; i++){
			if ( (i==0) | (i==4) | (i==5) |(i==6) |(i==7) |(i==8) |(i==14) |(i==15) | (i==18) ){
				String symbol=sentence_list[i].substring(0,1);
			    symbols.add(symbol);
			    map.put(symbol, i+1);
			}
			else{
				String symbol=sentence_list[i].substring(0,2);
				symbols.add(symbol);
			    map.put(symbol, i+1);
			}
		}
		for (int i = 0; i<symbols.size(); i++){
			System.out.print(symbols.get(i));
			System.out.println(map.get(symbols.get(i)));
		}
	}
}

