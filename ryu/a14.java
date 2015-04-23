import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class a14 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);

    	int LineCount = 0;
    	int linenumber = 10;
    	
    	String line = br.readLine();
    	while (line != null)
    	{
    		LineCount++;
    		if (LineCount > linenumber){
    			break;
    		}
    		System.out.println(line);
    		line = br.readLine();
    	}
        br.close();
    }
}