/**
 * 
 */
package knock_2015java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

/**
 * @author ryosuke
 *
 */
public class Knock004 extends Knock {
	String sent;
	ArrayList<Integer> head;
	HashMap<String, Integer> elem;

	/**
	 * 
	 */
	public Knock004() {
		sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
		head = new ArrayList<Integer>(Arrays.asList(1, 5, 6, 7, 8, 9, 15, 16, 19));
		elem = new HashMap<String, Integer>();
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		int i = 1;
		for(String tok: sent.split(" ")){

			if(head.contains(i)){
				tok = tok.substring(0, 1);
			}else{
				tok = tok.substring(0, 2);
			}
			elem.put(tok, i);
			i++;
		}

		// List 生成 (ソート用)
		List<Map.Entry<String,Integer>> entries = 
				new ArrayList<Map.Entry<String,Integer>>(elem.entrySet());
		Collections.sort(entries, new Comparator<Map.Entry<String,Integer>>() {
			@Override
			public int compare(
					Entry<String,Integer> entry1, Entry<String,Integer> entry2) {
				return ((Integer)entry1.getValue()).compareTo((Integer)entry2.getValue());
			}
		});
		
		for(Entry<String,Integer> e : entries){
			System.out.println(e.getKey()+":"+e.getValue());
		}
	}

}
