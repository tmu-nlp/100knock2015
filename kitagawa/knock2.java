/**
 * 
 */
package java_new100knock;

/**
 * @author kitagawayoshiaki
 *
 */
public class Knock2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		StringBuilder buf = new StringBuilder();
		String s1 = "パトカー";
		String s2 = "タクシー";

		for (int i=0; i<s1.length(); i++){
			buf.append(s1.charAt(i));
			buf.append(s2.charAt(i));
		}
		System.out.println(buf.toString());
		
	}

}
