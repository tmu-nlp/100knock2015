import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.TreeSet;

public class a17 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);
    	TreeSet<String> word_set = new TreeSet<String>();
    	
    	String line = br.readLine();
    	while (line != null) {
    		String[] words = line.split("	", 0);
    		word_set.add(words[0]);
    		line = br.readLine();
    	}
        br.close();
        
        Iterator<String> it = word_set.iterator();
        while (it.hasNext()) {
        	System.out.println(it.next());
        }
    }
}