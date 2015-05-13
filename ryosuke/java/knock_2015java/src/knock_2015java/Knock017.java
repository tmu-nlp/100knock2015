/**
 * 
 */
package knock_2015java;

import java.io.File;
import java.util.HashSet;

/**
 * @author ryosuke
 *
 */
public class Knock017 extends Knock {
	File inFile;
	HashSet<String> set;
	
	/**
	 * 
	 */
	public Knock017() {
		inFile = col1;
		set = new HashSet<String>();
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		for(String line : readFile(inFile)){
			set.add(line);
		}
		for(String s : set){
			System.out.println(s);
		}
	}

}
