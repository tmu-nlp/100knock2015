/**
 * 
 */
package knock_2015java;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * @author ryosuke
 *
 */
public class Knock005 extends Knock {
	public class Bigram{
		public Bigram(String f, String s){
			this.first = f;
			this.second = s;
		}
		public String first;
		public String second;
		
		public String getFirst() {
			return first;
		}
		public String getSecond() {
			return second;
		}
	}
	
	String sent;
	ArrayList<String> sent2;
	
	/**
	 * 
	 */
	public Knock005() {
		sent = "I am an NLPer";
		sent2 = new ArrayList<String>(Arrays.asList(sent.split(" ")));
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		System.out.println("word bigram");
		for(Bigram b : getWordBigram(sent)){
			System.out.println(b.getFirst()+" "+b.getSecond());
		}
		System.out.println();
		for(Bigram b : getWordBigram(sent2)){
			System.out.println(b.getFirst()+" "+b.getSecond());
		}
		
		System.out.println();
		System.out.println("character bigram");
		for(Bigram b : getCharBigram(sent)){
			System.out.println(b.getFirst()+" "+b.getSecond());
		}
		System.out.println();
		for(Bigram b : getCharBigram(sent2)){
			System.out.println(b.getFirst()+" "+b.getSecond());
		}
	}

	public ArrayList<Bigram> getWordBigram(String sent){
		String pretok = "<s>";
		String sent2 = sent + " </s>";
		ArrayList<Bigram> result = new ArrayList<Bigram>();
		for(String tok : sent2.split(" ")){
			result.add(new Bigram(pretok, tok));
			pretok = tok;
		}
		return result;
	}
	
	public ArrayList<Bigram> getWordBigram(ArrayList<String> sent){
		return getWordBigram(String.join(" ", sent));
	}
	
	public ArrayList<Bigram> getCharBigram(String sent){
		String pre_char = "<s>";
		ArrayList<Bigram> result = new ArrayList<Bigram>();
		for(int i = 0; i<sent.length(); i++){
			result.add(new Bigram(pre_char, String.valueOf(sent.charAt(i))));
			pre_char = String.valueOf(sent.charAt(i));
		}
		result.add(new Bigram(pre_char, "</s>"));
		return result;
	}
	
	public ArrayList<Bigram> getCharBigram(ArrayList<String> sent){
		return getCharBigram(String.join(" ", sent));
	}
}
