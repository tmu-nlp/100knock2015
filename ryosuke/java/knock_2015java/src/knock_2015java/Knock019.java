/**
 * 
 */
package knock_2015java;

import java.io.File;
import java.util.ArrayList;
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
public class Knock019 extends Knock {
	File inFile;
	HashMap<String, Integer> count;
	/**
	 * 
	 */
	public Knock019() {
		inFile = col1;
		count = new HashMap<String, Integer>();
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		for(String tok : readFile(inFile)){
			if(!count.containsKey(tok)){
				count.put(tok, 1);
			} else {
				count.put(tok, count.get(tok)+ 1);
			}
		}
		
		// List 生成 (ソート用)
		List<Map.Entry<String,Integer>> entries = 
				new ArrayList<Map.Entry<String,Integer>>(count.entrySet());
		Collections.sort(entries, new Comparator<Map.Entry<String,Integer>>() {
			@Override
			public int compare(
					Entry<String,Integer> entry1, Entry<String,Integer> entry2) {
				return ((Integer)entry2.getValue()).compareTo((Integer)entry1.getValue());
			}
		});
		
		for(Entry<String,Integer> e : entries){
			System.out.println(e.getKey()+":"+e.getValue());
		}
	}

}
