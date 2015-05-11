package knock_2015java;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;

public abstract class Knock {
	public File hightemp = new File("../../Data/hightemp.txt");
	public File col1 = new File("../../Data/col1.txt");
	public File col2 = new File("../../Data/col2.txt");
	public abstract void start();
	public void readFile(File inf){
		BufferedReader br;
		try {
			br = new BufferedReader(new FileReader(inf));
			String str;
			while(null != (str = br.readLine())){
				// yiled str　したい
			}
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
