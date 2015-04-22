/**
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
 */

/**
 * @author sakaisawayuya
 *
 */

import java.util.ArrayList;
import java.util.Collections;

public class Knock009 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		String sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .";
		ArrayList<String> result_list = new ArrayList<String>();
		for(String tok : sent.split(" ")){
			if(tok.length() <= 4){
				result_list.add(tok);
				continue;
			}
			ArrayList<Character> t = new ArrayList<Character>();
			StringBuffer sb = new StringBuffer();
			for(int i = 1; i<=tok.length()-2; i++){
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
		for(int i = 0; i<= result_list.size()-1; i++){
			System.out.print(result_list.get(i));
			if(i != result_list.size()-1){
				System.out.print(" ");	
			}
		}
	}

}
