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
		knock_list.add(new Knock007());
		knock_list.add(new Knock008());
		knock_list.add(new Knock009());
		knock_list.add(new Knock010());
		knock_list.add(new Knock011());
		knock_list.add(new Knock012());
		knock_list.add(new Knock013());
		knock_list.add(new Knock014(5));
		knock_list.add(new Knock015(5));
		knock_list.add(new Knock016(6));
		knock_list.add(new Knock017());
		knock_list.add(new Knock018());
		knock_list.add(new Knock019());
		
		knock_list.get(16).start();
	}

}
