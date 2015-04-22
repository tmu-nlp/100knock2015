/**
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
 */

/**
 * @author sakaisawayuya
 *
 */
public class Knock008 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		String s = "Test String";
		String Encode_s = "";
		String Decode_s = "";
		System.out.println(s);
		System.out.println("\nEncode");
		Encode_s = cipher(s);
		System.out.println(Encode_s);
		System.out.println("\nDecode");
		Decode_s = cipher(Encode_s);
		System.out.println(Decode_s);
	}
	public static String cipher(String s){
		StringBuffer sb = new StringBuffer();
		for (int i=0; i<s.length(); i++){
			if(Character.isLowerCase(s.charAt(i))){
				sb.append((char)(219 -  (int)s.charAt(i)));
			}else{
				sb.append(s.charAt(i));
			}
		}
		return s = sb.toString();
	}
}
