package knock_2015java;

public class Knock001 extends Knock {
	String tok;
	public Knock001(){
		tok = "パタトクカシーー";
	}
	@Override
	public void start() {
		System.out.printf("%c%c%c%c\n", tok.charAt(0), tok.charAt(2), tok.charAt(4), tok.charAt(6));
	}

}
