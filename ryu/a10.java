import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class a10 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);

    	int LineCount = 0;
    	String line = br.readLine();
    	while (line != null)
    	{
    		LineCount++;
    		line = br.readLine();
    	}
        System.out.println(LineCount);
        br.close();
    }
}