/**
 * 
 */
package knock_2015java;

import java.util.ArrayList;
import java.util.HashSet;

/**
 * @author ryosuke
 *
 */
public class Knock006 extends Knock {
	String tok1;
	String tok2;
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
		
		@Override
		public int hashCode(){
			return this.first.hashCode() + this.second.hashCode();
		}
		
		@Override
		public boolean equals(Object other) {
			if (this == other) {
				return true;
			}

			if (!(other instanceof Bigram)) {
				return false;
			}

			Bigram otherBigram = (Bigram) other;
			if (this.first.equals(otherBigram.getFirst()) && this.second.equals(otherBigram.getSecond())) {
				return true;
			}
			return false;
		}
	}
	/**
	 * 
	 */
	public Knock006() {
		tok1 = "paraparaparadise";
		tok2 = "paragraph";
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
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
}
