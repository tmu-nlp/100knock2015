/**
 * 02.「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ.
 */

/**
 * @author sakaisawayuya
 *
 */
public class Knock002 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		String src1, src2;
		StringBuffer sb;
		src1 = "パトカー";
		src2 = "タクシー";
		sb = new StringBuffer();
		
		for (int i=0; i<src1.length(); i++){
			sb.append(src1.charAt(i));
			sb.append(src2.charAt(i));
		}
		System.out.println(sb);

	}

}
