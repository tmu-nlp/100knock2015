package knock_2015java;

public class Knock001 extends Knock {
	String tok;
	public Knock001(){
		tok = "パタトクカシーー";
	}
	@Override
	public void start() {
		System.out.println(tok.substring(1, 2) + tok.substring(3, 4) + tok.substring(5, 6) + tok.substring(7, 8));
	}

}
