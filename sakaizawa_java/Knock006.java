/**
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
 */

/**
 * @author sakaisawayuya
 *
 */

import java.util.ArrayList;
import java.util.HashSet;

public class Knock006 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		String tok1 = "paraparaparadise";
		String tok2 = "paragraph";
		HashSet<Bigram> X = new HashSet<Bigram>(getCharBigram(tok1));
		HashSet<Bigram> Y = new HashSet<Bigram>(getCharBigram(tok2));
		HashSet<Bigram> XcupY = new HashSet<Bigram>(X);
		HashSet<Bigram> XcapY = new HashSet<Bigram>(X);
		HashSet<Bigram> XmY = new HashSet<Bigram>(X);
		HashSet<Bigram> YmX = new HashSet<Bigram>(Y);
		XcupY.addAll(Y);
		XcapY.retainAll(Y);
		XmY.removeAll(Y);
		YmX.removeAll(X);
		
		System.out.println("X");
		for(Bigram b : X){
			System.out.println(b.getFirst()+","+b.getSecond());
		}
		
		System.out.println("\nY");
		for(Bigram b : Y){
			System.out.println(b.getFirst()+","+b.getSecond());
		}

		System.out.println("\nX cup Y");
		for(Bigram b : XcupY){
			System.out.println(b.getFirst()+","+b.getSecond());
		}
		
		System.out.println("\nX cap Y");
		for(Bigram b : XcapY){
			System.out.println(b.getFirst()+","+b.getSecond());
		}
		
		System.out.println("\nX - Y");
		for(Bigram b : XmY){
			System.out.println(b.getFirst()+","+b.getSecond());
		}
		
		System.out.println("\nY - X");
		for(Bigram b : YmX){
			System.out.println(b.getFirst()+","+b.getSecond());
		}
	}

	public static ArrayList<Bigram> getCharBigram(String sent){
		String pre_char = "<s>";
		ArrayList<Bigram> result = new ArrayList<Bigram>();
		for(int i = 0; i<sent.length(); i++){
			result.add(new Bigram(pre_char, String.valueOf(sent.charAt(i))));
			pre_char = String.valueOf(sent.charAt(i));
		}
		result.add(new Bigram(pre_char, "</s>"));
		return result;
	}
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
		public String getSecond(){
			return second;
		}
		public int hashCode(){
			return this.first.hashCode() + this.second.hashCode();
		}
		public boolean equals(Object other){
			if (this == other){
				return true;
			}
			if (!(other instanceof Bigram)){
				return false;
			}
			Bigram otherBigram = (Bigram) other;
			if (this.first.equals(otherBigram.getFirst()) && this.second.equals(otherBigram.getSecond())) {
				return true;
			}
			return false;
		}
		
	}

}
