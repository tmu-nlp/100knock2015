/**
 * 
 */
package java_new100knock;

/**
 * @author kitagawayoshiaki
 *
 */
public class Knock1 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		StringBuilder buf = new StringBuilder();
	    String s1 = "パタトクカシーー";
	    for (int i=0; i<s1.length(); i=i+2){
	    	buf.append(s1.charAt(i));
	    }
	    System.out.println(buf.toString());
	}
}
