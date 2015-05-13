/**
 * 
 */
package knock_2015java;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author ryosuke
 *
 */
public class Knock011 extends Knock {

	BufferedReader br;
	Pattern pt;
	/**
	 * 
	 */
	public Knock011() {
		try {
			br = new BufferedReader(new FileReader(hightemp));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		pt = Pattern.compile("\t");
	}

	/* (非 Javadoc)
	 * @see knock_2015java.Knock#start()
	 */
	@Override
	public void start() {
		try {
			String str;
			while(null != (str = br.readLine())){
				Matcher m = pt.matcher(str);
				System.out.println(m.replaceAll(" "));
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}
