package knock_2015java;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

public abstract class Knock {
	public File hightemp = new File("../../Data/hightemp.txt");
	public File col1 = new File("../../Data/col1_java.txt");
	public File col2 = new File("../../Data/col2_java.txt");
	public File k13 = new File("../../Data/result_knock13_java.txt");
	public abstract void start();

	public void printFin(){
		System.out.println("fin");
	}
	
	public ArrayList<String> readFile(File inf){
		BufferedReader br;
		ArrayList<String> array = new ArrayList<String>();
		try {
			br = new BufferedReader(new FileReader(inf));
			String str;
			while(null != (str = br.readLine())){
				array.add(str);
			}
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return array;
	}

	public void printFile(File outf, String str, boolean a){
		try {
			PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(outf, a)));
			pw.print(str);
			pw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public ArrayList<MyPair> pyzip(ArrayList a1, ArrayList a2){
		ArrayList<MyPair> a = new ArrayList<MyPair>();
		for(int i = 0; i<a1.size(); i++){
			a.add(new MyPair(a1.get(i), a2.get(i)));
		}
		return a;
	}
}
