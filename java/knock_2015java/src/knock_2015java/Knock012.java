/**
 * 
 */
package knock_2015java;

import java.io.File;

/**
 * @author ryosuke
 *
 */
public class Knock012 extends Knock {
	public File inFile;
	public File outFile1;
	public File outFile2;
	
	/**
	 * 
	 */
	public Knock012() {
		inFile = hightemp;
		outFile1 = col1;
		outFile2 = col2;
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		for(String line : readFile(hightemp)){
			String[] spl = line.split("\t");
			printFile(outFile1, spl[0]+"\n", true);
			printFile(outFile2, spl[1]+"\n", true);
		}
		System.out.println("fin");
	}

}
