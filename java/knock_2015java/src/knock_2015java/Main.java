package knock_2015java;

import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		ArrayList<Knock> knock_list = new ArrayList<Knock>();
		knock_list.add(new Knock000());
		knock_list.add(new Knock001());
		knock_list.add(new Knock002());
		knock_list.add(new Knock003());
		knock_list.add(new Knock004());
		knock_list.add(new Knock005());
		knock_list.add(new Knock006());
		
		knock_list.get(6).start();
	}

}
