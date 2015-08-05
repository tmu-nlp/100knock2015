package knock_2015java;

public class Knock000 extends Knock{
	String tok;
	StringBuffer sb;
	public Knock000(){
		tok = "stressed";
		sb = new StringBuffer(tok);
	}
	
	@Override
	public void start(){
		System.out.println(sb.reverse().toString());
	}
}
