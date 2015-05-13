/**
 * 
 */
package knock_2015java;

import java.io.File;

/**
 * @author ryosuke
 *
 */
public class Knock013 extends Knock {
	public File inFile1;
	public File inFile2;
	public File outFile;
	
	/**
	 * 
	 */
	public Knock013() {
		inFile1 = col1;
		inFile2 = col2;
		outFile = k13;
	}
	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		for(MyPair p : pyzip(readFile(inFile1), readFile(inFile2))){
			printFile(outFile, p.get1()+"\t"+p.get2()+"\n", true);
		}
		printFin();
	}

}
