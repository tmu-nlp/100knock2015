import java.util.*;
import java.io.*;

//unix command: cut -f n file 
public class nlp17{
    public static void main(String[] args){
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(
                        new FileInputStream(args[0]),"UTF-8"));

			HashMap<String, Integer> dict = new HashMap<String, Integer>();
			for(String line=br.readLine(); line!=null; line=br.readLine()){
				String[] cells = line.split("\t");
				String cell  = cells[0];
				if(dict.containsKey(cell))
					dict.put(cell,dict.get(cell)+1);
				else
					dict.put(cell,1);
			}
			for(Iterator i=dict.keySet().iterator(); i.hasNext();){
				String cell = (String)i.next();
				System.out.println(cell);
			}

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
