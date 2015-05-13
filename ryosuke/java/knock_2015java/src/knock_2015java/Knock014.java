/**
 * 
 */
package knock_2015java;

import java.io.File;

/**
 * @author ryosuke
 *
 */
public class Knock014 extends Knock {

	int n;
	File inFile;
	int count;
	/**
	 * 
	 */
	public Knock014(int n) {
		this.n = n;
		inFile = hightemp;
		count = 0;
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		for(String line : readFile(inFile)){
			if(count == n){
				break;
			}
			System.out.println(line);
			count++;
		}
	}

}
