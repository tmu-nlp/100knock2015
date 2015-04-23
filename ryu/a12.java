import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class a12 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);
    	
    	File wf1 = new File("/Users/tachibanaryuichi/Documents/workspace/100knock2015/col1.txt");
    	File wf2 = new File("/Users/tachibanaryuichi/Documents/workspace/100knock2015/col2.txt");
    	
    	PrintWriter pw1 = new PrintWriter(new BufferedWriter(new FileWriter(wf1)));
    	PrintWriter pw2 = new PrintWriter(new BufferedWriter(new FileWriter(wf2)));

    	String line = br.readLine();
    	while (line != null)
    	{
    		String[] words = line.split("	", 0);
    		pw1.println(words[0]);
    		pw2.println(words[1]);
    		line = br.readLine();
    	}
        br.close();
        pw1.close();
        pw2.close();
    }
}