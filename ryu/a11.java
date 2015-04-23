import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class a11 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);

    	String line = br.readLine();
    	while (line != null)
    	{
    		String result = line.replaceAll("	", " ");
    		System.out.println(line);
    		System.out.println(result);
    		line = br.readLine();
    	}
        br.close();
    }
}