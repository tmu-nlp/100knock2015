/**
 * 
 */
package java_new100knock;

/**
 * @author kitagawayoshiaki
 *
 */
public class Knock8 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String strings = "I couldn't believe";
		String encode_str="";
		String decode_str="";
		encode_str=chipher(strings);
		decode_str=chipher(encode_str);
		System.out.println(encode_str);
		System.out.println(decode_str);

	}
	public static String chipher(String strings)  //関数
	{   
		String code_str = "";
		char[] charArray = strings.toCharArray();
		for (char ch : charArray) {
			if (Character.isLowerCase(ch)){
				int code;
				code = 219 - (int)ch;
				code_str = code_str + (char)code;
				
			}
			else{
				code_str = code_str+ch;
				
			}
		}
		return code_str;
	}

	public static boolean isLower(String str){
		return str.equals(str.toLowerCase());
	}
}
