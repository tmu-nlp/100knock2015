/**
 * 
 */
package knock_2015java;

import java.io.File;

/**
 * @author ryosuke
 *
 */
public class Knock016 extends Knock {
	File inFile;
	int line_count;
	int spl_num;
	int file_num;
	String file_name;
	File out;
	/**
	 * 
	 */
	public Knock016(int n) {
		inFile = hightemp;
		line_count = 0;
		for(String line : readFile(inFile)){
			line_count++;
		}
		
		spl_num = -(-line_count / n);
		line_count = 0;
		file_num = 0;
		file_name = "../../Data/knock016/java/%d.txt";
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		out = new File(String.format(file_name, file_num));
		for(String line : readFile(inFile)){
			if (line_count == spl_num){
				line_count = 0;
				file_num++;
				out = new File(String.format(file_name, file_num));
			}
				
			printFile(out, line+"\n", true);
			line_count++;
		}
		printFin();
	}

}
