package knock_2015java;

public class Knock001 extends Knock {
	String tok;
	public Knock001(){
		tok = "パタトクカシーー";
	}
	@Override
	public void start() {
		System.out.printf("%c%c%c%c\n", tok.charAt(1), tok.charAt(3), tok.charAt(5), tok.charAt(7));
	}

}
