import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class a15 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);
    	ArrayList<String> line_list = new ArrayList<String>();

    	int LineCount = 0;
    	int linenumber = 10;
    	int a;

    	String line = br.readLine();
    	while (line != null)
    	{
    		LineCount++;
    		line_list.add(line);
    		line = br.readLine();
    	}
    	br.close();
    	
    	if (LineCount >= linenumber){
    		a = LineCount - linenumber;
    	} else {
    		a = 0;
    	}
    	
    	for (int n = a;n < LineCount ;n++ ){
    		System.out.println(line_list.get(n));
    	}
    }
}