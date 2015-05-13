/**
 * 
 */
package knock_2015java;

import java.io.File;

/**
 * @author ryosuke
 *
 */
public class Knock015 extends Knock {
	File inFile;
	int n;
	int count;
	int all_count;
	/**
	 * 
	 */
	public Knock015(int n) {
		inFile = hightemp;
		this.n = n;
		all_count = 0;
		for(String line : readFile(inFile)){
			all_count += 1;
		}
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		for(String line : readFile(inFile)){
			if(count < all_count - n){
				count++;
				continue;
			}
			System.out.println(line);
		}
	}

}
