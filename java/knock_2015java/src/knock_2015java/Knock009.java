/**
 * 
 */
package knock_2015java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/**
 * @author ryosuke
 *
 */
public class Knock009 extends Knock {
	String sent;

	/**
	 * 
	 */
	public Knock009() {
		sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .";
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		ArrayList<String> result_list = new ArrayList<String>();
		for(String tok : sent.split(" ")){
			if(tok.length() <= 4){
				result_list.add(tok);
				continue;
			}
			ArrayList<Character> t = new ArrayList<Character>();
			StringBuffer sb = new StringBuffer();
			for(int i=1; i<=tok.length()-2; i++){
				t.add(tok.charAt(i));
			}
			Collections.shuffle(t);
			t.add(tok.charAt(tok.length()-1));
			t.add(0, tok.charAt(0));
			for(Character c : t){
				sb.append(c);
			}
			result_list.add(sb.toString());
			
		}
		
		System.out.println(sent);
		System.out.println(String.join(" ", result_list));
	}

}
