/**
 * 03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
 */

/**
 * @author sakaisawayuya
 *
 */

import java.util.ArrayList;

public class Knock003 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		String sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
		ArrayList<Integer> pi;
		pi = new ArrayList<Integer>();
		for (String s : sent.split(" ")){
			s = s.replace(",", "");
			s = s.replace(".", "");
			pi.add(s.length());
			
		}
		for (int i : pi){
			System.out.print(i);
		}
		
	}

}
