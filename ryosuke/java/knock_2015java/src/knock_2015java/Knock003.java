/**
 * 
 */
package knock_2015java;

import java.util.ArrayList;

/**
 * @author ryosuke
 *
 */
public class Knock003 extends Knock {
		String sent;
		ArrayList<Integer> pi;
		/**
	 * 
	 */
	public Knock003() {
		pi = new ArrayList<Integer>();
		sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		for (String s : sent.split(" ")){
			s = s.replace(".", "");
			s = s.replace(",", "");
			pi.add(s.length());
		}
		for (int i : pi){
			System.out.print(i);
		}
	}

}
