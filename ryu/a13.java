import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class a13 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr1 = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/col1.txt");
    	FileReader fr2 = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/col2.txt");
    	
    	BufferedReader br1 = new BufferedReader(fr1);
    	BufferedReader br2 = new BufferedReader(fr2);
    	
    	String line1 = br1.readLine();
    	String line2 = br2.readLine();
    	
    	String new_str1;
    	String new_str2;
    	
    	while (line1 != null)
    	{
    		new_str1 = line1.trim();
    		new_str2 = line2.trim();
    		System.out.printf("%s	%s\n", new_str1,new_str2);
    		line1 = br1.readLine();
    		line2 = br2.readLine();
    	}
    	
        br1.close();
        br2.close();
    }
}