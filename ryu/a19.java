import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;

public class a19 {
    public static void main(String argv[]) throws IOException {
    	FileReader fr = new FileReader("/Users/tachibanaryuichi/Documents/workspace/100knock2015/hightemp.txt");
    	BufferedReader br = new BufferedReader(fr);
    	HashMap<String, Integer> word_map = new HashMap<String, Integer>();
    	Integer put_int = 0;
    	
    	String line = br.readLine();
    	while (line != null) {
    		String[] words = line.split("	", 0);
    		if (word_map.containsKey(words[0])){ //defaultdictとか使えば短くなると思う
    			put_int = word_map.get(words[0]) + 1;
    			word_map.put(words[0],put_int);
    		}else {
    			word_map.put(words[0],1);
    		}    		
    		line = br.readLine();
    	}
        br.close();
        
        Iterator<String> it = word_map.keySet().iterator();
        while (it.hasNext()) {
        	Object o = it.next();
        	System.out.println(o + " = " + word_map.get(o));
        }
    }
}