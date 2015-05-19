/**
 * 
 */
package knock_2015java;

/**
 * @author ryosuke
 *
 */
public class Knock008 extends Knock {
	String s;
	/**
	 * 
	 */
	public Knock008() {
		s = "Test Stringa";
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		System.out.println(s);
		System.out.println("\nEncode");
		cipher();
		System.out.println(s);
		System.out.println("\nDecode");
		cipher();
		System.out.println(s);
	}

	public void cipher(){
		StringBuffer sb = new StringBuffer();
		for(int i=0; i<s.length(); i++){
			if(Character.isLowerCase(s.charAt(i))){
				sb.append((char)(219 - (int)s.charAt(i)));
			}else{
				sb.append(s.charAt(i));
			}
		}
		s = sb.toString();
	}
}
