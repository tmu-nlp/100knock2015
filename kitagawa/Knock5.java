/**
 * 
 */
package java_new100knock;

import java.util.ArrayList;
import java.util.List;

/**
 * @author kitagawayoshiaki
 *
 */
public class Knock5 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String sentence = "I am an NLPer";
		String[] sentence_list = sentence.split(" ", 0);
		List <String>char_bigram_list= new ArrayList<String>();
		List <String>word_bigram_list= new ArrayList<String>();
		//文字ngramの獲得
		for (int i=0; i<(sentence.length()-1); i++){
			char_bigram_list.add(sentence.substring(i,i+2));
		}
		//単語ngramの獲得
		for (int i=0; i<(sentence_list.length-1); i++){
			word_bigram_list.add(sentence_list[i]+" "+ sentence_list[i+1]);
		}
		//出力　確認
		for (int i=0; i<char_bigram_list.size(); i++){
			System.out.println(char_bigram_list.get(i));
		}
		for (int i=0; i<word_bigram_list.size(); i++){
			System.out.println(word_bigram_list.get(i));
		}
	}

}
