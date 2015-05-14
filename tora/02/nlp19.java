import java.util.*;
import java.io.*;

//unix command: cut -f 2<file | sort | uniq -c | sort -k 1 
public class nlp19{
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
			sort(dict);
			
		}catch (Exception e){
            e.printStackTrace();
        }
	}

	public static void sort(HashMap map){
		List<Map.Entry<String,Integer>> list = new LinkedList<Map.Entry<String,Integer>>();
		list.addAll(map.entrySet());
		Collections.sort(list, new Comparator<Map.Entry<String,Integer>>() {
			public int compare(Map.Entry obj1, Map.Entry obj2){
				int freq1 = (Integer)obj1.getValue();
				int freq2 = (Integer)obj2.getValue();
				if(freq1<freq2)
					return 1;
				else if(freq1==freq2)
					return 0;
				else
					return -1;
			}
		});

		for(Iterator<Map.Entry<String,Integer>> ite = list.iterator();ite.hasNext();){
			Map.Entry<String,Integer> cell = ite.next();
			System.out.printf("%s\t%d",(String)cell.getKey(),(Integer)cell.getValue());
			System.out.println();
		}
	}
}
