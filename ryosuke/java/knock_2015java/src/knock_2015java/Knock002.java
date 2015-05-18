package knock_2015java;

public class Knock002 extends Knock {
	String tok1, tok2;
	StringBuffer sb;
	
	public Knock002() {
		tok1 = "パトカー";
		tok2 = "タクシー";
		sb = new StringBuffer();
	}

	@Override
	public void start() {
		for (int i=0; i<tok1.length(); i++){
			sb.append(tok1.charAt(i));
			sb.append(tok2.charAt(i));
		}
		System.out.println(sb.toString());
	}

}
