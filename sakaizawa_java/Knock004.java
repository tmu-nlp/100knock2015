/**
 * 04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
 */

/**
 * @author sakaisawayuya
 *
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class Knock004 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		String sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
		ArrayList<Integer> head;
		HashMap<String, Integer> elem;
		head = new ArrayList<Integer>(Arrays.asList(1, 5, 6, 7, 8, 9, 15, 16, 19));
		elem = new HashMap<String, Integer>();
		int i = 1;
		for (String src : sent.split(" ")){
			if(head.contains(i)){
				src = src.substring(0, 1);
			}else{
				src = src.substring(0, 2);
			}
			elem.put(src, i);
			i++;
		}
		// List 生成 (ソート用)
		List<Map.Entry<String,Integer>> entries = 
				new ArrayList<Map.Entry<String,Integer>>(elem.entrySet());
		Collections.sort(entries, new Comparator<Map.Entry<String,Integer>>() {
			@Override
			public int compare(
					Entry<String,Integer> entry1, Entry<String,Integer> entry2) {
				return ((Integer)entry1.getValue()).compareTo((Integer)entry2.getValue());
			}
		});
		for(Entry<String,Integer> e : entries){
			System.out.println(e.getKey()+":"+e.getValue());

		}
	}
}