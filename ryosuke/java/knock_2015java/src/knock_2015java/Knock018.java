/**
 * 
 */
package knock_2015java;

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/**
 * @author ryosuke
 *
 */
public class Knock018 extends Knock {
	File inFile;
	/**
	 * 
	 */
	public Knock018() {
		inFile = hightemp;
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		ArrayList<String[]> l = new ArrayList<String[]>();
		for(String line : readFile(inFile)){
			l.add(line.split("\t", -1));
			System.out.println(line);
		}
		System.out.println();
		
		Collections.sort(l, new Comp());
		for(String[] s : l){
			System.out.println(String.join("\t", s));
		}
	}

	public class Comp implements Comparator<String[]>{
		@Override
		public int compare(String[] s1, String s2[]){
			return s2[2].compareTo(s1[2]);
		}
	}
}
