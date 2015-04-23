import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

public class a16 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);
    	ArrayList<String> line_list = new ArrayList<String>();

    	String wfp = "/Users/tachibanaryuichi/Documents/workspace/100knock2015/result_in_q16/01.txt";
    	File wf = new File(wfp);    	
    	PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(wf)));
    	float split_number;
    	float add_number;
    	int wfn = 1;
    	
    	float LineCount = 0;
    	float linenumber = 10; // この変数で分割数を決める

    	String line = br.readLine();
    	while (line != null)
    	{
    		LineCount++;
    		line_list.add(line);
    		line = br.readLine();
    	}
    	br.close();
    	
    	add_number = LineCount / linenumber;
    	split_number = add_number;

    	for (float n = 0;n < LineCount;n++){
    		if (split_number <= n){
    			pw.close();
    			wfn++;
    			split_number = split_number + add_number;
    			wfp = "/Users/tachibanaryuichi/Documents/workspace/100knock2015/result_in_q16/0" + String.valueOf(wfn) + ".txt";
    			wf = new File(wfp);
    			pw = new PrintWriter(new BufferedWriter(new FileWriter(wf)));
    		}
    		pw.println(line_list.get((int) n));
    	}
    	pw.close();
    }
}
